from django.urls import path
from . import views
app_name="projects"
urlpatterns=[
    path("",views.ProjectList.as_view(),name="list"),
    path("<int:pk>/",views.ProjectDetail.as_view(),name="detail"),
    path("new/",views.ProjectCreate.as_view(),name="create"),
    path("<int:pk>/edit/",views.ProjectUpdate.as_view(),name="update"),
    path("<int:pk>/delete/",views.ProjectDelete.as_view(),name="delete"),
    path("shots/new/",views.ScreenshotCreate.as_view(),name="shot_create"),
    path("shots/<int:pk>/edit/",views.ScreenshotUpdate.as_view(),name="shot_update"),
    path("shots/<int:pk>/delete/",views.ScreenshotDelete.as_view(),name="shot_delete"),
]