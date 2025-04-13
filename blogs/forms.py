from django import forms
from .models import BlogPost, Forum, Comment  # Added Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'forum', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your post title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your blog post here'}),
            'forum': forms.Select(),
        }

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter forum name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe the forum'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)