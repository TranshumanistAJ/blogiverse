from django.shortcuts import render, get_object_or_404, redirect  # Added redirect
from .models import Forum, BlogPost
from .forms import BlogPostForm  # Import the form
from django.contrib.auth.decorators import login_required  # For login restriction

# Existing views
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

# New view for creating posts
@login_required  # Ensure only logged-in users can create posts
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)  # Include FILES for photo upload
        if form.is_valid():
            blog_post = form.save(commit=False)  # Don’t save yet
            blog_post.author = request.user  # Set the logged-in user as author
            blog_post.save()  # Save the post
            return redirect('topic_list', forum_name=blog_post.forum.name)  # Redirect to forum
    else:
        form = BlogPostForm()  # Empty form for GET request
    return render(request, 'blogs/create_post.html', {'form': form})