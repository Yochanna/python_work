from django import forms
from .models import Page

class PageForm(forms.ModelForm):                 # [form]
    class Meta:
        model = Page                             # [model]
        fields = ["title", "content"]            # [fields]
