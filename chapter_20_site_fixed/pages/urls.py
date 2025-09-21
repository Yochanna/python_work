from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.page_list, name="page_list"),      # [route-list]
    path("add/", views.add_page, name="add_page"),    # [route-add]
]
