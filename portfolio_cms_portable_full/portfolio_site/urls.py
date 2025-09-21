from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls", namespace="projects")),
    path("", RedirectView.as_view(pattern_name="projects:list", permanent=False)),
]