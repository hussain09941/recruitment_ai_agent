from django.urls import path
from . import views

urlpatterns = [
    # --- Job posting ---
    path('post/', views.post_job, name='post_job'),

    # --- Job listing & details ---
    path('list/', views.job_list, name='job_list'),
    path('detail/<int:job_id>/', views.job_detail, name='job_detail'),

    # --- Job application ---
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),

    # --- Recruiter similarity-based match ---
    path('best_candidates/<int:job_id>/', views.best_candidates, name='best_candidates'),
]
