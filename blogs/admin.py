from django.contrib import admin
from .models import BlogPost

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author")

admin.site.register(BlogPost, BlogAdmin)