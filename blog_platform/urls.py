from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
    path('blogs/<str:forum_name>/', views.topic_list, name='topic_list'),
    path('blogs/post/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('blogs/create/', views.create_post, name='create_post'),
    path('blogs/post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('blogs/post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('blogs/create-forum/', views.create_forum, name='create_forum'),  # New URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)