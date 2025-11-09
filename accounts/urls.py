from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('candidate/dashboard/', views.candidate_dashboard, name='candidate_dashboard'),
    path('company/dashboard/', views.company_dashboard, name='company_dashboard'),
]
