from django.contrib import admin
from .models import BlogPost, Forum, Comment

admin.site.register(BlogPost)
admin.site.register(Forum)
admin.site.register(Comment)