# blog_platform/urls.py
# Main URL configuration for Blogiverse project

from django.contrib import admin  # Imports admin interface for site management
from django.urls import path, include  # Imports path for URL patterns, include for routing
from django.conf import settings  # Imports settings for media/static URLs
from django.conf.urls.static import static  # Serves media files during development
from blogs import views  # Imports views from blogs app (correct source for view functions)

# Defines project-wide URL 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('create/', views.create_post, name='create_post'),
    path('create-forum/', views.create_forum, name='create_forum'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),  # ✅ This was missing
    path('<str:forum_name>/', views.topic_list, name='topic_list'),  # Keep this LAST
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
