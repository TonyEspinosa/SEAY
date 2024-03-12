from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'admin123'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
#     ]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}