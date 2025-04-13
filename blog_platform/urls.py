from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_list, name='home'),
    path('<str:forum_name>/', views.topic_list, name='topic_list'),
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_forum/', views.create_forum, name='create_forum'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
]