from django.urls import path
from . import views

urlpatterns = [
    path('upvote/<int:paper_id>/', views.upvote, name='upvote'),
    path('comment/<int:paper_id>/', views.add_comment, name='add_comment'),
]
