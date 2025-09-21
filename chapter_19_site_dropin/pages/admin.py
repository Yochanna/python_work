from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "date_added")
    search_fields = ("title", "content")
    ordering = ("-date_added",)
