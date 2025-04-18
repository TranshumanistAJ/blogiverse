# blogs/views.py
# This file contains view functions handling HTTP requests and rendering templates for the blogs app.

from django.shortcuts import render, get_object_or_404, redirect  # Imports utilities for rendering templates, fetching objects, and redirecting
from django.contrib.auth.decorators import login_required  # Imports decorator to restrict views to authenticated users
from django.contrib import messages  # Imports messages framework for user feedback
from django.http import JsonResponse  # Imports JsonResponse for AJAX responses (e.g., like counts)
from .models import Forum, BlogPost, Comment  # Imports models for forums, posts, and comments
from .forms import BlogPostForm, ForumForm, CommentForm  # Imports forms for creating/editing posts, forums, and comments

# Displays the homepage with all forums
def home(request):
    forums = Forum.objects.all()  # Fetches all forums from the database
    return render(request, 'index.html', {'forums': forums})  # Renders index.html with forums context

# Lists posts, optionally filtered by forum
def topic_list(request, forum_name=None):
    if forum_name:  # If a forum name is provided in the URL
        forum = get_object_or_404(Forum, name=forum_name)  # Fetches forum or returns 404
        posts = BlogPost.objects.filter(forum=forum)  # Filters posts by forum
    else:  # If no forum specified
        posts = BlogPost.objects.all()  # Fetches all posts
    return render(request, 'blogs/topic_list.html', {'forum': forum if forum_name else None, 'posts': posts})  # Renders topic_list.html

# Displays a single post with comments and comment form
def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)  # Fetches post by ID or returns 404
    comments = Comment.objects.filter(post=post)  # Fetches all comments for the post
    comment_form = CommentForm()  # Initializes an empty comment form
    if request.method == 'POST':  # If form is submitted
        comment_form = CommentForm(request.POST)  # Populates form with POST data
        if comment_form.is_valid():  # Validates form
            comment = comment_form.save(commit=False)  # Creates comment instance without saving
            comment.post = post  # Assigns post to comment
            comment.author = request.user  # Assigns current user as author
            comment.save()  # Saves comment to database
            messages.success(request, "Comment added!")  # Shows success message
            return redirect('blog_detail', post_id=post.id)  # Redirects to same post
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})  # Renders post_detail.html

# Handles post creation, restricted to logged-in users
@login_required
def create_post(request):
    if request.method == 'POST':  # If form is submitted
        form = BlogPostForm(request.POST, request.FILES)  # Populates form with POST and file data
        if form.is_valid():  # Validates form
            post = form.save(commit=False)  # Creates post instance without saving
            post.author = request.user  # Assigns current user as author
            post.save()  # Saves post to database
            messages.success(request, "Post created successfully!")  # Shows success message
            return redirect('blog_detail', post_id=post.id)  # Redirects to new post
    else:  # If GET request
        form = BlogPostForm()  # Initializes empty form
    return render(request, 'blogs/create_post.html', {'form': form})  # Renders create_post.html

# Handles forum creation, restricted to logged-in users
@login_required
def create_forum(request):
    if request.method == 'POST':  # If form is submitted
        form = ForumForm(request.POST)  # Populates form with POST data
        if form.is_valid():  # Validates form
            forum = form.save()  # Saves forum to database
            messages.success(request, "Forum created successfully!")  # Shows success message
            return redirect('topic_list', forum_name=forum.name)  # Redirects to new forum
    else:  # If GET request
        form = ForumForm()  # Initializes empty form
    return render(request, 'blogs/create_forum.html', {'form': form})  # Renders create_forum.html

# Handles post editing, restricted to post author
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)  # Fetches post by ID and author or returns 404
    if request.method == 'POST':  # If form is submitted
        form = BlogPostForm(request.POST, request.FILES, instance=post)  # Populates form with POST, files, and existing post
        if form.is_valid():  # Validates form
            form.save()  # Updates post in database
            messages.success(request, "Post updated successfully!")  # Shows success message
            return redirect('blogs/blog_detail', post_id=post.id)  # Redirects to updated post
    else:  # If GET request
        form = BlogPostForm(instance=post)  # Initializes form with existing post data
    return render(request, 'blogs/edit_post.html', {'form': form, 'post': post})  # Renders edit_post.html

# Handles post deletion, restricted to post author
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)  # Fetches post by ID and author or returns 404
    if request.method == 'POST':  # If form is submitted
        post.delete()  # Deletes post from database
        messages.success(request, "Post deleted successfully!")  # Shows success message
        return redirect('topic_list', forum_name=post.forum.name)  # Redirects to forum
    return render(request, 'blogs/delete_post.html', {'post': post})  # Renders delete_post.html

# Handles liking/unliking posts, restricted to logged-in users
@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)  # Fetches post by ID or returns 404
    if request.user in post.likes.all():  # If user has already liked
        post.likes.remove(request.user)  # Removes like
        messages.success(request, "Like removed.")  # Shows success message
    else:  # If user hasn’t liked
        post.likes.add(request.user)  # Adds like
        messages.success(request, "Post liked!")  # Shows success message
    return JsonResponse({'likes_count': post.likes.count()})  # Returns updated like count for AJAX

# Handles adding comments, restricted to logged-in users
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)  # Fetches post by ID or returns 404
    if request.method == 'POST':  # If form is submitted
        content = request.POST.get('content')  # Gets comment content from POST data
        if content:  # If content is not empty
            Comment.objects.create(post=post, author=request.user, content=content)  # Creates new comment
            messages.success(request, "Comment added!")  # Shows success message
    return redirect('blogs/blog_detail', post_id=post_id)  # Redirects to post