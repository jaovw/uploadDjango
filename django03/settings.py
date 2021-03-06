"""
Django settings for django03 project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import pytz
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y#l)_s2$xsr7swkz0g6pc71sro03$&(#&1m(wgg96%d%y636!b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #criados por mim 
    'component',
    'crispy_forms',
    'accounts',
    'anymail',
    
    
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

ROOT_URLCONF = 'django03.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'django03.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
   'default': {
        'NAME': BASE_DIR / 'db.sqlite3', #antiga base j?? incluida na pasta 
        'ENGINE': 'django.db.backends.sqlite3',
        #caso necessite a implementa????o e utiliza????o do mySQL
        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'django',
        #'USER': 'root',
        #'PASSWORD': '',
        #'HOST': '127.0.0.1',
        #'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')

]
MEDIA_URL = "/media/"
MEDIAFILES_DIR = [
    os.path.join(BASE_DIR, 'media')
     ]
'''
ROOTDIR = os.path.dirname(__file__)

ADMIN_MEDIA_PREFIX = '/admin_media/'

DEBUG = True
TEMPLATE_DEBUG = DEBUG'''
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

### EMAIL ###

from decouple import config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.googlemail.com'
#EMAIL_HOST = 'smtplw.com.br'
EMAIL_HOST = 'email-ssl.com.br'
EMAIL_USE_TLS = True
#EMAIL_USE_SSL = True
EMAIL_PORT = 587
#EMAIT_PORT = 465
EMAIL_HOST_USER = 'no-reply@superfestval.com.br'
EMAIL_HOST_PASSWORD = 'F3stv@l999'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
