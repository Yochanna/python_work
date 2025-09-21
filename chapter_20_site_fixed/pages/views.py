from django.shortcuts import render, redirect
from .models import Page
from .forms import PageForm

def page_list(request):                           # [list-view]
    pages = Page.objects.order_by('date_added')
    return render(request, "pages/page_list.html", {"pages": pages})

def add_page(request):                            # [create-view]
    if request.method == "POST":                  # [branch]
        form = PageForm(request.POST)             # [bind]
        if form.is_valid():                       # [validate]
            form.save()                           # [save]
            return redirect("pages:page_list")    # [redirect]
    else:
        form = PageForm()                         # [empty-form]
    return render(request, "pages/add_page.html", {"form": form})   # [render]
