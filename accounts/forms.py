from django import forms
from django.contrib.auth.models import User
from .models import CompanyProfile, CandidateProfile




# --- User Registration Form ---
class UserRegisterForm(forms.ModelForm):
    USER_TYPES = (
        ('candidate', 'Candidate'),
        ('company', 'Company'),
    )

    user_type = forms.ChoiceField(choices=USER_TYPES, label="Register As")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'user_type']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

# --- Candidate Profile Form ---
class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['full_name', 'resume', 'skills', 'education', 'experience']

# --- Company Profile Form ---
class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'industry', 'website', 'description']



