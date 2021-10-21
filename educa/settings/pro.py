from .base import *
from educa.settings.local import DATABASES, DEBUG
import os

DEBUG = False


ALLOWED_HOSTS = ['*', ]

ADMINS = (
    ('morteza mousakhani', 'khodemousa@gmail.com'),
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],

    }
}
