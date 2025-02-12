from django.db import models
from django.conf import settings

class ResearchPaper(models.Model):
    title = models.CharField(max_length=200)
    uploaded_file = models.FileField(upload_to='research_papers/')
    description = models.TextField()
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    short_video = models.URLField(blank=True, null=True)  # URL to short video
    long_video = models.URLField(blank=True, null=True)   # URL to long video

    def __str__(self):
        return self.title
