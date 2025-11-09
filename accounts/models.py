# models.py

from django.db import models
from django.contrib.auth.models import User

# --- 1. Company Profile ---
class CompanyProfile(models.Model):
    # This ensures a 1:1 link with the standard Django User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
    
    # Specific Company attributes
    company_name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"Company Profile for {self.company_name}"

# --- 2. Candidate Profile ---
class CandidateProfile(models.Model):
    # This ensures a 1:1 link with the standard Django User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')
    
    # Specific Candidate attributes
    full_name = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(help_text="Comma-separated list of skills", blank=True)
    education = models.CharField(max_length=255, blank=True)
    experience = models.CharField(max_length=255, blank=True, help_text="Example: 2 years in Python Development")
    def __str__(self):
        return f"Candidate Profile for {self.full_name}"