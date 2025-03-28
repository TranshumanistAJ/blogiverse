from django import forms
from .models import BlogPost, Forum  # Added Forum

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'forum', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your post title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your blog post here'}),
            'forum': forms.Select(),
        }

# New form for Forum
class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter forum name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe the forum'}),
        }