from django.contrib import admin
from .models import Project,Screenshot
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=("title","status","date_added")
    list_filter=("status","date_added")
    search_fields=("title","blurb","repo_url","demo_url")
@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display=("project","caption","image_url")
    search_fields=("project__title","caption")