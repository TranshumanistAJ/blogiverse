# blog_platform/urls.py
# Main URL configuration for Blogiverse project

from django.contrib import admin  # Imports admin interface for site management
from django.urls import path, include  # Imports path for URL patterns, include for routing
from django.conf import settings  # Imports settings for media/static URLs
from django.conf.urls.static import static  # Serves media files during development
from blogs import views  # Imports views from blogs app (correct source for view functions)

# Defines project-wide URL patterns
urlpatterns = [
    # Routes '/admin/' to Django admin site for managing users, posts, etc.
    path('admin/', admin.site.urls),
    # Includes allauth URLs for authentication (login, signup, logout, etc.)
    path('accounts/', include('allauth.urls')),
    # Root URL ('') maps to blogs home view, showing all forums
    path('', views.home, name='home'),
    # Routes forum-specific posts (e.g., /Personal-Growth/)
    path('<str:forum_name>/', views.topic_list, name='topic_list'),
    # Routes individual post details (e.g., /post/1/)
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
    # Routes post creation
    path('create/', views.create_post, name='create_post'),
    # Routes forum creation
    path('create-forum/', views.create_forum, name='create_forum'),
    # Routes post editing
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    # Routes post deletion
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    # Routes post liking
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    # Routes comment addition
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serves media (e.g., blog photos) in dev