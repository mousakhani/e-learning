from .base import *
from educa.settings.local import DATABASES, DEBUG
from .secure_keys import *

DEBUG = False


ALLOWED_HOSTS = ['localhost', ]

ADMINS = (
    ('morteza mousakhani', 'khodemousa@gmail.com'),
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
    }
}
