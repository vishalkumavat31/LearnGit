from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_research_paper, name='upload_research_paper'),
    path('profile/<str:username>/', views.user_profile, name='profile'),
]
