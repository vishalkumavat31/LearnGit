# interactions/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Vote, Comment
from papers.models import ResearchPaper

@login_required
def upvote(request, paper_id):
    paper = ResearchPaper.objects.get(id=paper_id)
    existing_vote = Vote.objects.filter(paper=paper, user=request.user).first()
    
    if existing_vote:
        existing_vote.delete()  # Remove previous vote if any
    
    Vote.objects.create(paper=paper, user=request.user, is_upvote=True)  # Add a new upvote
    return redirect('profile', username=request.user.username)

@login_required
def add_comment(request, paper_id):
    if request.method == 'POST':
        paper = ResearchPaper.objects.get(id=paper_id)
        text = request.POST['comment_text']
        Comment.objects.create(paper=paper, user=request.user, text=text)
    return redirect('profile', username=request.user.username)
