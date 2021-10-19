from .base import *
from educa.settings.local import DATABASES, DEBUG


DEBUG = False


ALLOWED_HOSTS = ['*']

ADMINS = (
    ('morteza mousakhani', 'khodemousa@gmail.com'),
)


DATABASES = {
    'default': {

    }
}
