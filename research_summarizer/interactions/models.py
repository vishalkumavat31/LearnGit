from django.db import models
from django.conf import settings
from papers.models import ResearchPaper

class Vote(models.Model):
    paper = models.ForeignKey(ResearchPaper, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_upvote = models.BooleanField()

    def __str__(self):
        return f"{self.user.username} {'upvoted' if self.is_upvote else 'downvoted'} {self.paper.title}"

class Comment(models.Model):
    paper = models.ForeignKey(ResearchPaper, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.paper.title}"
