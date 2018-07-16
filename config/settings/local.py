import raven

from .base import *  # noqa

DEBUG = True
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
SECRET_KEY = 'l0cedol28)9tt$1ridf4sr*!!us=9iqn@rvn2l^qoovy#)pubb'


INSTALLED_APPS += ['django.contrib.staticfiles', 'raven.contrib.django.raven_compat']
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
STATIC_URL = '/static/'



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


RAVEN_CONFIG = {
    'dsn': 'http://74417134beee46819996a5a52763abe7:bede877d315e4a68864d8a8cb81fdcad@localhost:9000/2',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(BASE_DIR)),
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


