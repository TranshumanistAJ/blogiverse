# blogs/models.py
# This file defines the data models for forums, blog posts, and comments, structuring the database.

from django.db import models  # Imports Django's model framework for database interaction
from django.contrib.auth.models import User  # Imports User model for authentication
from django.utils import timezone
import uuid, os
from cloudinary.models import CloudinaryField

def unique_blog_photo_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('blog_photos', filename)

# Defines the Forum model for categorizing posts
class Forum(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Unique name for the forum (e.g., "Personal Growth")
    description = models.TextField(blank=True)  # Optional description of the forum’s purpose

    def __str__(self):
        return self.name  # Returns forum name as string representation

# Defines the BlogPost model for user-created posts
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Unique title for the post
    content = models.TextField()  # Main body of the post
    #photo = models.ImageField(upload_to=unique_blog_photo_path, blank=True, null=True) # to upload image with unique address
        
    photo = CloudinaryField('image', blank=True, null=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Links post to user, deletes post if user is deleted
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)  # Links post to forum, deletes post if forum is deleted
    created_at = models.DateTimeField(default=timezone.now)  # Auto-sets creation timestamp
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)  # Tracks users who liked the post

    def __str__(self):
        return self.title  # Returns post title as string representation

# Defines the Comment model for user comments on posts
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)  # Links comment to post, deletes if post is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Links comment to user, deletes if user is deleted
    content = models.TextField()  # Comment text
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-sets creation timestamp

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"  # Returns comment summary as string