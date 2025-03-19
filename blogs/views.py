from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def topic_list(request, topic):
    posts = BlogPost.objects.filter(topic=topic)
    return render(request, 'blogs/topic_list.html', {'posts': posts, 'topic': topic})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blogs/blog_detail.html', {'post': post})