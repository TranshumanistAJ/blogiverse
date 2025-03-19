from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from blogs.views import topic_list, blog_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('blogs/<str:topic>/', topic_list, name='topic_list'),
    path('blogs/post/<int:post_id>/', blog_detail, name='blog_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)