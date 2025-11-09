from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Application
from .forms import JobForm
from accounts.models import CompanyProfile, CandidateProfile

# ✅ Local resume text extractor
#from .utils import extract_text_from_resume

# ✅ AI cosine similarity from ai_engine
#from ai_engine.utils import match_resume_to_job
from ai_engine.utils import extract_text_from_resume, match_resume_to_job


# -------------------------------
# 🏢 COMPANY: POST A JOB
# -------------------------------
@login_required
def post_job(request):
    try:
        company = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        messages.error(request, "Access denied — only companies can post jobs.")
        return redirect('job_list')

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.save()
            messages.success(request, "✅ Job posted successfully!")
            return redirect('company_dashboard')
    else:
        form = JobForm()

    return render(request, 'jobs/post_job.html', {'form': form})


# -------------------------------
# 👨‍💼 CANDIDATE: APPLY FOR A JOB
# -------------------------------
@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    try:
        candidate_profile = CandidateProfile.objects.get(user=request.user)
    except CandidateProfile.DoesNotExist:
        messages.error(request, "Access denied — only candidates can apply for jobs.")
        return redirect('job_list')

    # ✅ Check if already applied
    if Application.objects.filter(candidate=candidate_profile, job=job).exists():
        messages.warning(request, "You have already applied for this job.")
        return redirect('job_detail', job_id=job.id)

    if request.method == 'POST':
        resume = request.FILES.get('resume')
        cover_letter = request.POST.get('cover_letter')

        Application.objects.create(
            candidate=candidate_profile,
            job=job,
            resume=resume or candidate_profile.resume,
            cover_letter=cover_letter,
        )

        messages.success(request, "🎯 Application submitted successfully!")
        return redirect('job_detail', job_id=job.id)

    return render(request, 'jobs/apply_job.html', {'job': job})


# -------------------------------
# 🧠 COMPANY: AI BASED RESUME MATCHING
# -------------------------------
@login_required
def best_candidates(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    # ✅ Only job owner can view
    if not hasattr(request.user, 'company_profile') or job.company.user != request.user:
        messages.error(request, "Access denied — only the job owner can view candidates.")
        return redirect('job_list')

    applications = Application.objects.filter(job=job)
    results = []

    for app in applications:
        if app.resume:
            resume_text = extract_text_from_resume(app.resume.path)

            score = match_resume_to_job(job.skills_required, resume_text)

            results.append({
                'candidate': app.candidate,
                'score': score,  # already % based
                'resume': app.resume.url if app.resume else None,
                'applied_at': app.applied_at
            })

    # ✅ Sort by similarity score
    results.sort(key=lambda x: x['score'], reverse=True)

    top_n = int(request.GET.get('top', 5))
    top_candidates = results[:top_n]

    return render(request, 'jobs/best_candidates.html', {
        'job': job,
        'results': results,
        'top_candidates': top_candidates,
        'top_n': top_n
    })


# -------------------------------
# 📋 JOB LIST
# -------------------------------
def job_list(request):
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


# -------------------------------
# 🔍 JOB DETAILS
# -------------------------------
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})


# -------------------------------
# 🏢 COMPANY DASHBOARD
# -------------------------------
@login_required
def company_dashboard(request):
    try:
        company = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        messages.error(request, "Access denied — only companies can access this dashboard.")
        return redirect('job_list')

    jobs = Job.objects.filter(company=company).order_by('-created_at')
    return render(request, 'jobs/company_dashboard.html', {
        'company': company,
        'jobs': jobs
    })


# ---------------------------------------------------
# ✅ Resume Filter (standalone simple filter)
# ---------------------------------------------------
@login_required
def filter_resumes(request, job_id):
    job = Job.objects.get(id=job_id)
    candidates = CandidateProfile.objects.filter(resume__isnull=False)

    matches = []

    for candidate in candidates:
        resume_text = extract_text_from_resume(candidate.resume.path)

        score = match_resume_to_job(job.skills_required, resume_text)

        matches.append({
            'candidate': candidate,
            'score': score
        })

    matches.sort(key=lambda x: x['score'], reverse=True)

    return render(request, 'jobs/resume_filter_results.html', {
        'job': job,
        'matches': matches
    })
