from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ResearchPaperForm
from .models import ResearchPaper
from django.contrib.auth.decorators import login_required

@login_required
def upload_research_paper(request):
    if request.method == 'POST':
        form = ResearchPaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.uploaded_by = request.user
             # Call your video summarization logic here (e.g., a background task or API call)
            paper.short_video = generate_short_video(paper.uploaded_file) #
            paper.long_video = generate_long_video(paper.uploaded_file) #
            paper.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ResearchPaperForm()
    return render(request, 'papers/upload.html', {'form': form})

@login_required
def user_profile(request, username):
    user = request.user
    papers = ResearchPaper.objects.filter(uploaded_by=user)
    return render(request, 'users/profile.html', {'user': user, 'papers': papers})
