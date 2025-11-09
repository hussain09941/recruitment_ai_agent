from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserRegisterForm, CandidateProfileForm, CompanyProfileForm
from .models import CandidateProfile, CompanyProfile
from jobs.models import Job


# 🧾 Registration View
'''def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        user_type = request.POST.get('user_type')  # should match template field name

        # Choose profile form based on user type
        if user_type == 'company':
            profile_form = CompanyProfileForm(request.POST, request.FILES)
        else:
            profile_form = CandidateProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Save user
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Save profile linked to user
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # ✅ Success message
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        else:
            # Show errors if invalid
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserRegisterForm()
        profile_form = CandidateProfileForm()  # default form
        user_type = 'candidate'

    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_type': user_type,
    })
'''




'''def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        user_type = request.POST.get('user_type')  # company or candidate

        if user_type == 'company':
            profile_form = CompanyProfileForm(request.POST, request.FILES)
        else:
            profile_form = CandidateProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # ✅ Save user type in profile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # ✅ Add success message
            messages.success(request, f"Registration successful as {user_type.title()}! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserRegisterForm()
        profile_form = CandidateProfileForm()
        user_type = 'candidate'

    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_type': user_type,
    })


# 🔐 Login View
'def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            # Redirect based on profile type
            if hasattr(user, 'candidateprofile'):
                return redirect('candidate_dashboard')
            elif hasattr(user, 'companyprofile'):
                return redirect('company_dashboard')
            else:
                logout(request)
                messages.error(request, "No profile found for this user.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'accounts/login.html')

'''



'''def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        user_type = request.POST.get('user_type')  # should exist in your HTML form

        if user_type == 'company':
            profile_form = CompanyProfileForm(request.POST, request.FILES)
        else:
            profile_form = CandidateProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Save User
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Create the right profile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # ✅ Confirm user type visually
            messages.success(request, f"🎉 Registration successful as {user_type.title()}! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        user_form = UserRegisterForm()
        profile_form = CandidateProfileForm()
        user_type = 'candidate'

    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_type': user_type,
    })
'''


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        user_type = request.POST.get('user_type')  # candidate or company
        print("POST DATA:", request.POST)
        print("USER TYPE SENT:", request.POST.get('user_type'))
        print("TOGGLE USER TYPE:", request.POST.get('toggleUserType'))

        # Select the right profile form based on user type
        if user_type == 'company':
            profile_form = CompanyProfileForm(request.POST, request.FILES)
        else:
            profile_form = CandidateProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Save User
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Save profile linked to user
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, f"🎉 Registration successful as {user_type.title()}! You can now log in.")
            return redirect('login')
        else:
            # Collect all errors
            errors = user_form.errors.as_json() + profile_form.errors.as_json()
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        user_form = UserRegisterForm()
        profile_form = CandidateProfileForm()
        user_type = 'candidate'
        errors = None

    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_type': user_type,
        'errors': errors
    })

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        # Allow both email and username for login
        try:
            user_obj = User.objects.get(email=username_or_email)
            username = user_obj.username
        except User.DoesNotExist:
            username = username_or_email

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            # Redirect based on profile type
            if hasattr(user, 'candidate_profile'):
                return redirect('candidate_dashboard')
            elif hasattr(user, 'company_profile'):
                return redirect('company_dashboard')
            else:
                logout(request)
                messages.error(request, "No profile found for this user.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'accounts/login.html')


# 🚪 Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')


# 👨‍💼 Candidate Dashboard
@login_required
def candidate_dashboard(request):
    try:
        profile = CandidateProfile.objects.get(user=request.user)
    except CandidateProfile.DoesNotExist:
        messages.error(request, "You do not have a candidate profile.")
        return redirect('company_dashboard')

    jobs = Job.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'accounts/candidate_dashboard.html', {'jobs': jobs})


# 🏢 Company Dashboard
@login_required
def company_dashboard(request):
    try:
        profile = CompanyProfile.objects.get(user=request.user)
    except CompanyProfile.DoesNotExist:
        messages.error(request, "You do not have a company profile.")
        return redirect('candidate_dashboard')

    jobs = Job.objects.filter(company=profile).order_by('-created_at')
    return render(request, 'accounts/company_dashboard.html', {'jobs': jobs})
