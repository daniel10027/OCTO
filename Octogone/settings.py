import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CSRF_TRUSTED_ORIGINS = ['https://octogone.tech','http://octogone.tech']

CSRF_COOKIE_SECURE=True

X_FRAME_OPTIONS = "SAMEORIGIN"

SILENCED_SYSTEM_CHECKS = ["security.W019"]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-272)m*d+9#d!u^egva0#ds043*-#5g-&l7w%x)a&k1$*xp=-1w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sites',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Octogone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Octogone.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
if DEBUG:
    db = "postgres"
else:
    db = "daniel"

DATABASES = {
                "default": {
                    "ENGINE": "django.db.backends.postgresql_psycopg2",
                    "NAME": "octogone",
                    "USER": db,
                    "PASSWORD": "10027563",
                    "HOST": "127.0.0.1",
                    "PORT": "5432",
                    }
}

if DEBUG:
    
    STATIC_URL = 'static/'
    MEDIA_URL = 'media/'
    STATIC_ROOT = os.path.join(BASE_DIR,'static')
    MEDIA_ROOT = os.path.join(BASE_DIR,'media')
    
else: 
    
    STATIC_URL = 'static/'
    MEDIA_URL = 'media/'
    STATIC_ROOT = "/home/daniel/IIPEACOM/static/"
    STATICFILES_DIR = "/home/daniel/IIPEACOM/static/"
    MEDIA_ROOT = "/home/daniel/IIPEACOM/media/"


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'FR-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
