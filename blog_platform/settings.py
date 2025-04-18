# blog_platform/settings.py
# Django project settings for Blogiverse

from pathlib import Path
import os
import dj_database_url

# Load env.py if present for local development
if os.path.isfile('env.py'):
    import env

# Base directory for project
BASE_DIR = Path(__file__).resolve().parent.parent
# Templates directory
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Security settings
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True
print('DEBUG: ', DEBUG)
ALLOWED_HOSTS = ['8000-transhumanis-blogiverse-viuld5f44ox.ws-eu118.gitpod.io', 'https://blogiverse-a5563d85b65c.herokuapp.com', 'https://blogiverse-a5563d05b65c.herokuapp.com'] if not DEBUG else ['localhost', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://blogiverse-a5563d85b65c.herokuapp.com']

# Installed apps for Django functionality
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin interface
    'django.contrib.auth',  # Authentication system
    'django.contrib.contenttypes',  # Content types framework
    'django.contrib.sessions',  # Session management
    'django.contrib.messages',  # Messages framework
    'cloudinary_storage',  # Cloudinary media storage
    'django.contrib.staticfiles',  # Static file handling
    'cloudinary',  # Cloudinary integration
    'django.contrib.sites',  # Sites framework for allauth
    'allauth',  # Allauth authentication
    'allauth.account',  # Allauth account features
    'allauth.socialaccount',  # Allauth social auth
    'django_summernote',  # Summernote editor for posts
    'crispy_forms',  # Crispy forms for styling
    'blogs',  # Your blogs app
]

# Allauth site ID
SITE_ID = 1
# Disable email verification
ACCOUNT_EMAIL_VERIFICATION = 'none'
# Redirects after login/logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default Django auth
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth auth
]

# Middleware for request processing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security enhancements
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static file serving
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session handling
    'django.middleware.common.CommonMiddleware',  # Common utilities
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # User auth
    'allauth.account.middleware.AccountMiddleware',  # Allauth middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Frame protection
]

# Root URL configuration
ROOT_URLCONF = 'blog_platform.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # Custom templates dir
        'APP_DIRS': True,  # Loads app templates
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Debug info
                'django.template.context_processors.request',  # Request data
                'django.contrib.auth.context_processors.auth',  # User auth
                'django.contrib.messages.context_processors.messages',  # Messages
            ],
        },
    },
]

# WSGI application for deployment
WSGI_APPLICATION = 'blog_platform.wsgi.application'

# Database configuration from environment
DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}

# Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Bootstrap message tags
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static file settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media file settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Cloudinary configuration
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME', 'blogiverse'),  # Your cloud name
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY', '247894279316566'),  # Your API key
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET', 'iRiz-uxfJn4o_W2JvpWXFJjVXIw'),  # Your API secret
}

# Summernote and crispy forms settings
SUMMERNOTE_THEME = 'bs4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
X_FRAME_OPTIONS = 'SAMEORIGIN'  # For Summernote in production
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'