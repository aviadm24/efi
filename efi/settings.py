"""
Django settings for efi project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
import socket

#user name Efi
# password: eficaneti

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bjotijs+h#(ew1#+r!+1wj1g11bi3_*zuxfqg)a-h=p46z148+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['caneti.herokuapp.com', '127.0.0.1', 'scenic-dry-tortugas-44462.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'main',
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'bootstrapform',
    'django_extensions',
    'django_tables2',
    'import_export',
]
#took out
#'bootstrap_datepicker',
# 'django_select2',

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'efi.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'efi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
ipaddress = socket.gethostbyname(socket.gethostname())
print('ip_address:', ipaddress)
if not ipaddress.startswith('172'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {}
    DATABASES['default'] =  dj_database_url.config()



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

# importent to be able to use date format!
USE_L10N = False

USE_TZ = True

# https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#std:templatefilter-date
# https://stackoverflow.com/questions/1513502/django-how-to-format-a-datefields-date-representation
# DATE_INPUT_FORMAT = '%m/%d/%Y'
DATE_INPUT_FORMATS = ('%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y', '%d/%m/%Y', '%Y/%m/%d', '%A, %B %d %Y')
DATE_FORMATS = ('%A, %B %d %Y', '%Y-%m-%d', '%m/%d/%Y')
# DATETIME_INPUT_FORMATS = ('%m/%d/%Y %H:%M',)
DATETIME_FORMAT = 'n/j/Y G:i'
# https://stackoverflow.com/questions/28049010/modifying-display-format-of-datetimes-in-django-tables2
SHORT_DATETIME_FORMAT = 'n/j/Y H:i'
# SHORT_DATE_FORMAT = 'l, F d, Y'
TIME_FORMAT = 'G:i'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

if not ipaddress.startswith('172'):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'aviadm32@gmail.com'
    EMAIL_HOST_PASSWORD = 'aviadpython'
    EMAIL_PORT = 587
else:
    # https://github.com/sklarsa/django-sendgrid-v5
    EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
    SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]
    SENDGRID_SANDBOX_MODE_IN_DEBUG = False

# new staging env in heroku https://scenic-dry-tortugas-44462.herokuapp.com/ deployed to Heroku


LOGIN_REDIRECT_URL = 'main_list'