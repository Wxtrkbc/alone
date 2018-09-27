"""
Django base settings for ins project.

"""

import os

from ins.utils.log import get_log_config


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'l0cedol28)9tt$1ridf4sr*!!us=9iqn@rvn2l^qoovy#)pubb'


DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'django_filters'
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
    # 'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
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
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend', ),

    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}

LOG_PATH = os.getenv('LOG_PATH', '/tmp/log/alone/')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
LOG_HANDLER = os.getenv('LOG_HANDLER', 'debug,error,info,color').split(',')
LOGGING = get_log_config('alone', LOG_HANDLER, LOG_LEVEL, LOG_PATH)

APPEND_SLASH = False

COS_SECRET_ID = os.getenv('COS_SECRET_ID')
COS_SECRET_KEY = os.getenv('COS_SECRET_KEY')



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'postgres'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432')
    }
}

REDIS = {
    'host': os.getenv('REDIS_HOST', '127.0.0.1'),
    'port': os.getenv('REDIS_PORT', 6379)
}


ELASTICSEARCH_DSL = {
    'default': {
        'hosts': '{}:{}'.format(os.getenv('ELASTICSEARCH_HOST', 'localhost'),
                                os.getenv('ELASTICSEARCH_HOST_PORT', 9200))
    },
}


if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYD_TASK_TIME_LIMIT = 5 * 60
CELERYD_TASK_SOFT_TIME_LIMIT = 60


EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.qq.com')
EMAIL_PORT = os.getenv('EMAIL_PORT', 25)
EMAIL_FROM = os.getenv('EMAIL_FROM', 'melodywangdong@foxmail.com')
EMAIL_USE_TLS = True


MQ_USERNAME = os.getenv('MQ_USERNAME', 'guest')
MQ_PASSWORD = os.getenv('MQ_USERNAME', 'guest')
MQ_HOST = os.getenv('MQ_HOST', 'localhost')
MQ_VIRTUAL_HOST = os.getenv('MQ_VIRTUAL_HOST', '/')
MQ_PORT = os.getenv('MQ_PORT', )