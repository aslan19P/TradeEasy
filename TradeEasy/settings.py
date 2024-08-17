"""
Django settings for TradeEasy project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wgs*ep20@6w&1sl%(3a1x%qc=*i#14ppmd=v%^fpmxs=s(v0(_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1', '*']


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'django_extensions',
    
    'orders',
    'cart',
    'products',
    'users',
    'payment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TradeEasy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'TradeEasy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aslan',
        'USER': 'aslan',
        'PASSWORD': 'apajan123',
    }
}

CSRF_TRUSTED_ORIGINS = [
    'https://83b1-84-54-83-43.ngrok-free.app',
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


LANGUAGES = [
    ('ru', _('Russian')),
    ('en', _('English')),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'

LOCALE_PATHS =[
    BASE_DIR / 'locale',
] 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CART_SESSION_ID = 'cart'


LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
]

from .ton  import *

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = user
EMAIL_HOST_PASSWORD = password
EMAIL_PORT = 587
EMAIL_USE_TLS = True


SOCIAL_AUTH_FACEBOOK_KEY = kesface 
SOCIAL_AUTH_FACEBOOK_SECRET = secretface
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


SOCIAL_AUTH_TWITTER_KEY = keyx
SOCIAL_AUTH_TWITTER_SECRET = secretx

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = keygoog
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = secretgoog


SOCIAL_AUTH_GITHUB_KEY = keygit
SOCIAL_AUTH_GITHUB_SECRET = secretgit
SOCIAL_AUTH_GITHUB_SCOPE = ['email']



STRIPE_PUBLISHABLE_KEY = 'pk_test_51PombD04KEbzbnGGaZiArS6BaAkaTxz6vFaetzv7eEKAiwy0fwyWdNaiookw8Zh89G7i3DlFs2aonhUahFtpHlHD00ttW3PiI1' # Публикуемый ключ
STRIPE_SECRET_KEY = 'sk_test_51PombD04KEbzbnGGh8O3jPUMJO6hz30kacEcjBqgWwWPQs1SpqCTqdt299ct5l3PdVtjOvvb8YjeE0te0Qgvsh3r00tQWrmslm'
# Секретный ключ
STRIPE_API_VERSION = '2022-08-01'

STRIPE_WEBHOOK_SECRET = 'whsec_229965368998e7a09c6466b793307ab994b0956f6d394e5498e14e874ac11736'