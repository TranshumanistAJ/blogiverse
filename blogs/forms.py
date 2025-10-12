# blogs/forms.py
# This file defines forms for creating/editing blog posts, forums, and comments.

from django import forms  # Imports Django’s forms framework
from .models import BlogPost, Forum, Comment  # Imports models for form validation


# Form for creating/editing blog posts
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost  # Links form to BlogPost model
        fields = ['title', 'content', 'forum', 'photo']  # Specifies fields to include
        widgets = {
            # Customizes title field with placeholder
            'title': forms.TextInput(attrs={'placeholder': 'Enter your post title'}),
            # Customizes content field with placeholder
            'content': forms.Textarea(attrs={'placeholder': 'Write your blog post here'}),
            # Uses dropdown for forum selection
            'forum': forms.Select(),
        }  # Defines input widgets for better UX


# Form for creating/editing forums
class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum  # Links form to Forum model
        fields = ['name', 'description']  # Specifies fields to include
        widgets = {
            # Customizes name field with placeholder
            'name': forms.TextInput(attrs={'placeholder': 'Enter forum name'}),
            # Customizes description field with placeholder
            'description': forms.Textarea(attrs={'placeholder': 'Describe the forum'}),
        }  # Defines input widgets for clarity


# Form for adding comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Links form to Comment model
        fields = ('content',)  # Only includes content field
        widgets = {
            # Customizes content field with placeholder
            'content': forms.Textarea(attrs={'placeholder': 'Add your comment'}),
        }  # Enhances UX with clear prompt
