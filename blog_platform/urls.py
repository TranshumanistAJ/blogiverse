# blogs/urls.py
# This file defines URL patterns specific to the blogs app, mapping URLs to views.

from django.urls import path  # Imports path for defining URL routes
from . import views  # Imports views from the blogs app to handle requests

# Defines URL patterns for the blogs app
urlpatterns = [
    # Root URL ('') maps to home view, displaying all forums
    path('', views.home, name='home'),
    # '/create/' maps to create_post view for new blog posts
    path('create/', views.create_post, name='create_post'),
    # '/create-forum/' maps to create_forum view for new forums
    path('create-forum/', views.create_forum, name='create_forum'),
    # '/post/<post_id>/' maps to blog_detail view for specific post details
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
    # '/post/<post_id>/edit/' maps to edit_post view for updating posts
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    # '/post/<post_id>/delete/' maps to delete_post view for removing posts
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    # '/<forum_name>/' maps to topic_list view for forum-specific posts
    path('<str:forum_name>/', views.topic_list, name='topic_list'),
    # '/like/<post_id>/' maps to like_post view for toggling likes
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    # '/comment/<post_id>/' maps to add_comment view for adding comments
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
]