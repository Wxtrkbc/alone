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

MIDDLEWARE += ['raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware', ]

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


RAVEN_CONFIG = {
    'dsn': os.getenv('RAVEN_DSN',
                     'http://74417134beee46819996a5a52763abe7:bede877d315e4a68864d8a8cb81fdcad@localhost:9000/2'),
    # 'release': raven.fetch_git_sha(os.path.dirname(BASE_DIR)),
}



