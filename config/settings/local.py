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

# RAVEN_CONFIG = {
#     'dsn': 'http://625a75bfb1164a269d44e555efa46c5f:430a10e003f1447baee5d75a0c55c793@172.18.0.6/2',
#     # 'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
# }