from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from accounts.models import CandidateProfile
from jobs.models import Job
from .utils import extract_text_from_resume, match_resume_to_job


def filter_resumes(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    candidates = CandidateProfile.objects.filter(resume__isnull=False)
    resumes = []

    for cand in candidates:
        resume_text = extract_text_from_resume(cand.resume.path)
        score = match_resume_to_job(job.description + " " + job.skills_required, resume_text)

        resumes.append({
            "candidate": cand,
            "score": score,
            "applied_at": cand.user.date_joined,
        })

    # ✅ Search filter
    query = request.GET.get("q", "")
    if query:
        resumes = [
            m for m in resumes
            if query.lower() in m["candidate"].full_name.lower()
        ]

    # ✅ Sort by score
    sort_order = request.GET.get("sort", "desc")
    if sort_order == "asc":
        resumes.sort(key=lambda x: x["score"])
    else:
        resumes.sort(key=lambda x: x["score"], reverse=True)

    # ✅ Pagination
    paginator = Paginator(resumes, 5)  # 5 results per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'ai_engine/match_results.html', {
        "job": job,
        "page_obj": page_obj,
        "query": query,
        "sort_order": sort_order,
    })
