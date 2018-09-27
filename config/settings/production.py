from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = [
    "132.232.2.205",
]

DJANGO_SETTINGS_MODULE = os.getenv("DJANGO_SETTINGS_MODULE",
                                   "config.settings.local")



