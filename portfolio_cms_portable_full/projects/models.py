from django.db import models
class Project(models.Model):
    STATUS_CHOICES=[("draft","Draft"),("in_progress","In Progress"),("published","Published"),("archived","Archived")]
    title=models.CharField(max_length=200)
    blurb=models.TextField(blank=True)
    repo_url=models.URLField(blank=True)
    demo_url=models.URLField(blank=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="draft")
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["-date_added"]
    def __str__(self): return self.title
class Screenshot(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name="screenshots")
    image_url=models.URLField(blank=True)
    caption=models.CharField(max_length=200,blank=True)
    def __str__(self): return f"{self.project.title} — {self.caption or 'Screenshot'}"