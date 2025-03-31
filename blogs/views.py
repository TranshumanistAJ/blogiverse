from django.shortcuts import render, get_object_or_404, redirect
from .models import Forum, BlogPost
from .forms import BlogPostForm, ForumForm  # Added ForumForm
from django.contrib.auth.decorators import login_required

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

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('topic_list', forum_name=blog_post.forum.name)
    else:
        form = BlogPostForm()
    return render(request, 'blogs/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.author != request.user:
        return redirect('blog_detail', post_id=post.id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogs/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.author != request.user:
        return redirect('blog_detail', post_id=post.id)
    if request.method == 'POST':
        forum_name = post.forum.name
        post.delete()
        return redirect('topic_list', forum_name=forum_name)
    return render(request, 'blogs/delete_post.html', {'post': post})


@login_required
def create_forum(request):
    if not request.user.is_staff:  
        return redirect('home')
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ForumForm()
    return render(request, 'blogs/create_forum.html', {'form': form})