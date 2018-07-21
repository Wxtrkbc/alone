"""
Django base settings for ins project.

"""

import os

from ins.utils.log import get_log_config


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders'
]

LOCAL_APPS = [
    'ins.app',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # log 404 events to the Sentry server.
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',

    # alone exception
    'ins.middleware.AloneExceptionMiddleware'
]

ROOT_URLCONF = 'ins.urls'

WSGI_APPLICATION = 'ins.wsgi.application'


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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


API_VERSION = 'v1'
AUTH_USER_MODEL = 'app.User'
AUTHENTICATION_BACKENDS = [
    'ins.user.auth.AloneBackend'
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

LOG_PATH = os.getenv('LOG_PATH', '/tmp/log/alone/')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
LOG_HANDLER = os.getenv('LOG_HANDLER', 'debug,error,info,color').split(',')
LOGGING = get_log_config('alone', LOG_HANDLER, LOG_LEVEL, LOG_PATH)
