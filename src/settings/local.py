try:
    from .base import *
except ImportError:
    print("Can't import base settings")

DEBUG = True

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
