from omgtt.configs.common.settings import *
import logging


DEBUG = False
TEMPLATE_DEBUG = DEBUG
SITE_DOMAIN = 'omg.tt'
MEDIA_URL = 'http://media.omg.tt/media/'
MEDIA_URL_BASE = 'http://media.omg.tt'

GOOGLE_SITE_VERIFY_CODE = 'qmLyWZ_8zbkzTbKmNae-A25MRrMdzrCw3Kxgx9NCato'


ADMIN_MEDIA_PREFIX = '/static/admin/'
DOWNLOAD_DIRECTORY = '/tmp/'

SITE_ID = "4f290a9016d5ad05fd00001d"

INTERNAL_IPS = ()

DATABASES = {
        'default': {
            'ENGINE': 'django_mongodb_engine',
            'NAME': 'omgtt',
            'TEST_NAME': 'omgtt_test',
            'HOST': 'omg-mongo1.demo.gd,omg-mongo2.demo.gd,omg-mongo3.demo.gd',
            }
        }

TWITTER = {
        'ZH':{
            'CONSUMER_KEY':'GkX6g6ww83bxzmyebEgW7A',
            'CONSUMER_SECRET':'j9KN0ghpI0QBR8j0LaUrxJG6bbj8FUpcQ7I40DOpQ1Y',
            'ACCESS_TOKEN':'550738353-0OI0NaD9m7ysijNbHDHBOlPQeZ1WpuHgXbiFQvei',
            'ACCESS_TOKEN_SECRET':'RfMrITeU53TrnEJHdsEJE4sESlgEIpsbMIct7vNyGg',
            },
        'EN':{
            'CONSUMER_KEY':'sQGeEtI8efY8gOrDxeiZBQ',
            'CONSUMER_SECRET':'32IPrrP8E2gPkcrrYPVexpIwSVLT9e6ld8Cb44VRk',
            'ACCESS_TOKEN':'478300776-HCaW4qSCkZaot3HnWc3n9fZ3umUmR90TEoP419Gj',
            'ACCESS_TOKEN_SECRET':'mDUEBJSQRkD0VFRwVLPd6CoFWEz5UvJFrBUJ79hK0',
            },
        'JP':{
            'CONSUMER_KEY':'5bDVGlhWDLXc8KEKK7b4Q',
            'CONSUMER_SECRET':'FejHNX7g6HyTsUo991e4agx9Wu5WJwwi4YMjakx4mQ',
            'ACCESS_TOKEN':'478498293-ViqNjzYtoU5sw3zs9tJaclP3x5cDuBmBRhPPFx2b',
            'ACCESS_TOKEN_SECRET':'dtU4d9Hk09mQxrJIMQuEFOEPHiAgrkp8APYmbzJ9XU',
            },
}

FACEBOOK = {
        'API':{
            'KEY':'285862821467049',
            'SECRET':'20afb8cec15cfb7a236d855ba9e32141',
            'APP_ID':'285862821467049',
            },
        'USER':{
            'ID':'100003616651753',
            'ACCESS_TOKEN':'AAAEDZCZAZCtk6kBAImmEfrXJKbucMSnDF864BRFZB0OFlZAtny5HcduVYtki0SxCm3iZCtcZC6fqZBxPrcaRz1IaYBqNeQq7sZCxuhbmBqIj74AZDZD',
            },
        'PAGES':{
            'ZH':{
                'ID':'358232870864805',
                'ACCESS_TOKEN':'AAAEDZCZAZCtk6kBADlcWwfyaQLIGvLjNcLwk0Ua3l9uOiL2THZA0b041qKbryQ52Q2125i9mtaqManGp4Y1Va870vyIBhdV09A6uELJ9O6GsqfzTJZBZBx',
                },
            'EN':{
                'ID':'335909009779912',
                'ACCESS_TOKEN':'AAAEDZCZAZCtk6kBABnlkGKRszphQQzZCwyOOBZCXr8evJ6XR2ghJKSVKTZAdowXPZASOsBwoX7awZCjsYdvrYUylDJq54oZBepwaFhlfzWptxK9xlUvxCJuYx',
                },
            'JP':{
                'ID':'121060244689828',
                'ACCESS_TOKEN':'AAAEDZCZAZCtk6kBAIR4obO3qdJOJVgcH77VwMufgrv7JZBBEaQbsjLvT3Bv6UZAEdP8qhRJYUZChovcH7RaxpBWKnp9X6jSPl8k39PuVRpU6jh4gTs1HRB',
                },
            },
        }

USE_LESS = False

FEED_IMPORT_TARGET_SITE = "http://omg.demo.gd:1337"

logging.basicConfig(level=logging.DEBUG)

