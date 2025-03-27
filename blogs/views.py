from django.shortcuts import render, get_object_or_404
from .models import Forum, BlogPost

def home(request):
    forums = Forum.objects.all()
    return render(request, 'index.html', {'forums': forums})

def topic_list(request, forum_name):
    forum = get_object_or_404(Forum, name=forum_name)
    posts = BlogPost.objects.filter(forum=forum)
    return render(request, 'blogs/topic_list.html', {'forum': forum, 'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blogs/blog_detail.html', {'post': post})