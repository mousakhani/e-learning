from .base import *
from educa.settings.local import DATABASES, DEBUG


DEBUG = False


ALLOWED_HOSTS = ['*', ]

ADMINS = (
    ('morteza mousakhani', 'khodemousa@gmail.com'),
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'mA12#',

    }
}
