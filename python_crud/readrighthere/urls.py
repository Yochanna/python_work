from django.urls import path
from . import views
urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('new/', views.article_create, name='article_create'),
    path('<int:pk>/edit/', views.article_update, name='article_update'),
    path('<int:pk>/delete/', views.article_delete, name='article_delete'),
]
