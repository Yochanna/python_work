from django.shortcuts import render                    # [import]
from .models import Page                               # [import-model]

def page_list(request):                                # [view]
    pages = Page.objects.order_by('date_added')        # [query]
    return render(request, "pages/page_list.html", {"pages": pages})  # [render]
