from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'forum', 'photo']  # Fields for users to fill
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your post title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your blog post here'}),
            'forum': forms.Select(),  
        }