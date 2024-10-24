from django.contrib import admin
from django.urls import path, include
from . import views
from .views import profile_view, edit_post

urlpatterns = [
    path('http_response/', views.http_response),
    path('html_response/', views.html_response),
    path('post/', views.post_list_view),
    path('post/<int:post_id>/', views.post_detail_view),
    path('create/', views.create_post),
    path('success/', views.post_success),
    path('profile/', profile_view),
    path('post/<int:post_id>/edit/', edit_post),
]
