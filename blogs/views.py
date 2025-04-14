from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Forum, BlogPost, Comment
from .forms import BlogPostForm, ForumForm, CommentForm

def home(request):
    forums = Forum.objects.all()
    return render(request, 'index.html', {'forums': forums})

def topic_list(request, forum_name=None):
    if forum_name:
        forum = get_object_or_404(Forum, name=forum_name)
        posts = BlogPost.objects.filter(forum=forum)
    else:
        posts = BlogPost.objects.all()
    return render(request, 'topic_list.html', {'forum': forum if forum_name else None, 'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added!")
            return redirect('blog_detail', post_id=post.id)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('blog_detail', post_id=post.id)
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save()
            messages.success(request, "Forum created successfully!")
            return redirect('topic_list', forum_name=forum.name)
    else:
        form = ForumForm()
    return render(request, 'create_forum.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('blog_detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('topic_list', forum_name=post.forum.name)
    return render(request, 'delete_post.html', {'post': post})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        messages.success(request, "Like removed.")
    else:
        post.likes.add(request.user)
        messages.success(request, "Post liked!")
    return JsonResponse({'likes_count': post.likes.count()})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
            messages.success(request, "Comment added!")
    return redirect('blog_detail', post_id=post_id)