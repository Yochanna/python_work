from django import forms
from .models import Project,Screenshot
class ProjectForm(forms.ModelForm):
    class Meta: model=Project; fields=["title","blurb","repo_url","demo_url","status"]
class ScreenshotForm(forms.ModelForm):
    class Meta: model=Screenshot; fields=["project","image_url","caption"]