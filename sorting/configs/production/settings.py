from sorting.configs.common.settings import *
import logging


DEBUG = False
TEMPLATE_DEBUG = DEBUG
SITE_DOMAIN = 'www.card-sorting.com'
MEDIA_URL = 'http://www.card-sorting.com/media/'
MEDIA_URL_BASE = 'http://www.card-sorting.com'


ADMIN_MEDIA_PREFIX = '/static/admin/'
DOWNLOAD_DIRECTORY = '/tmp/'

SITE_ID = "4f290a9016d5ad05fd00001d"

INTERNAL_IPS = ()

DATABASES = {
        'default': {
            'ENGINE': 'django_mongodb_engine',
            'NAME': 'sorting',
            'TEST_NAME': 'sorting_test',
            }
        }

USE_LESS = False


logging.basicConfig(level=logging.DEBUG)

