from django.db import models
from django.utils import timezone
from accounts.models import CompanyProfile, CandidateProfile


# --- Job Model ---
class Job(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills_required = models.TextField(help_text="Enter comma-separated skills, e.g. Python, Django, REST API")
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    experience_required = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self):
        return f"{self.title} — {self.company.company_name}"

    def skill_list(self):
        """Return clean list of required skills"""
        return [s.strip().lower() for s in self.skills_required.split(',') if s.strip()]


# --- Application Model ---
class Application(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='applications/resumes/', blank=True, null=True)
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(default=timezone.now)
    cosine_similarity_score = models.FloatField(default=0.0, help_text="Used for AI-based resume filtering")

    class Meta:
        ordering = ['-applied_at']
        verbose_name = "Application"
        verbose_name_plural = "Applications"
        unique_together = ('candidate', 'job')  # prevent duplicate applications

    def __str__(self):
        return f"{self.candidate.full_name} → {self.job.title}"
