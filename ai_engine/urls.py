from django.urls import path
from . import views

urlpatterns = [
    path('filter/<int:job_id>/', views.filter_resumes, name='filter_resumes'),
]
