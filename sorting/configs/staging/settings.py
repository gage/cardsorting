from omgtt.configs.common.settings import *
import logging


DEBUG = True
TEMPLATE_DEBUG = DEBUG
SITE_DOMAIN = 'omg.demo.gd:1337/'
MEDIA_URL = 'http://omg.demo.gd:1337/media/'


ADMIN_MEDIA_PREFIX = '/static/admin/'
DOWNLOAD_DIRECTORY = '/tmp/'

SITE_DOMAIN = 'omg.demo.gd:1337'
#"omg.demo.gd"
SITE_ID = "4f0534c016d5ad4cce00001d"

#"mongo1, mongo2 (production)
#SITE_ID = "4f0534c016d5ad4cce00001d"

INTERNAL_IPS = ()
"""
DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'omgtt',
        'TEST_NAME': 'omgtt_test',
        'HOST': 'omg-mongo1.demo.gd,omg-mongo2.demo.gd',
    }
}
"""

TWITTER = { 
        'ZH':{
            'CONSUMER_KEY':'cGhoWHRA9aiZFGHdiGA',
            'CONSUMER_SECRET':'e2U3lnB7UFRiujWQoXQtP9I5BpGYwtm7r5mKt2PYA8',
            'ACCESS_TOKEN':'533645764-LaIgZk5voAVdDMq7BvIdXBZpc4TryfFhMPlaHmuL',
            'ACCESS_TOKEN_SECRET':'gubHiVjtmoRJLmgkEiUQ2QA66da2RMbg23CPXT7Cms',
            },  
        'EN':{
            'CONSUMER_KEY':'cGhoWHRA9aiZFGHdiGA',
            'CONSUMER_SECRET':'e2U3lnB7UFRiujWQoXQtP9I5BpGYwtm7r5mKt2PYA8',
            'ACCESS_TOKEN':'533645764-LaIgZk5voAVdDMq7BvIdXBZpc4TryfFhMPlaHmuL',
            'ACCESS_TOKEN_SECRET':'gubHiVjtmoRJLmgkEiUQ2QA66da2RMbg23CPXT7Cms',
            },  
        'JP':{
            'CONSUMER_KEY':'cGhoWHRA9aiZFGHdiGA',
            'CONSUMER_SECRET':'e2U3lnB7UFRiujWQoXQtP9I5BpGYwtm7r5mKt2PYA8',
            'ACCESS_TOKEN':'533645764-LaIgZk5voAVdDMq7BvIdXBZpc4TryfFhMPlaHmuL',
            'ACCESS_TOKEN_SECRET':'gubHiVjtmoRJLmgkEiUQ2QA66da2RMbg23CPXT7Cms',
            },  
}


FACEBOOK = { 
        'API':{
            'KEY':'172593759495024',
            'SECRET':'6e8e86173e4101faba3c2a3fed49e24f',
            'APP_ID':'172593759495024',
            },  
        'USER':{
            'ID':'100000503406934',
            'ACCESS_TOKEN':'AAACcZBR25o3ABAAmlWa1jzQas4HFWIJjDISnlTv7CaqogCrydMwpaFZCCmNuhTHZCVI39TkAcDduUPQiKrRR2PMkZA3NtrktoweS0RwhrgZDZD',
            },  
        'PAGES':{
            'ZH':{
                'ID':'251518078252162', 
                'ACCESS_TOKEN':'AAACcZBR25o3ABAEE8QYZB5YmuCtgWZBUZAYuxZB35Y2rKGSxDIJySQMrxZAaCbKZArYHqZBONtkTqNwtmmct0VzHCV64xej2qN3wUIAXKZA9BZADJW2T1ZCUbCZC',
                },  
            'EN':{
                'ID':'251518078252162',
                'ACCESS_TOKEN':'AAACcZBR25o3ABAEE8QYZB5YmuCtgWZBUZAYuxZB35Y2rKGSxDIJySQMrxZAaCbKZArYHqZBONtkTqNwtmmct0VzHCV64xej2qN3wUIAXKZA9BZADJW2T1ZCUbCZC',
                },  
            'JP':{
                'ID':'251518078252162',
                'ACCESS_TOKEN':'AAACcZBR25o3ABAEE8QYZB5YmuCtgWZBUZAYuxZB35Y2rKGSxDIJySQMrxZAaCbKZArYHqZBONtkTqNwtmmct0VzHCV64xej2qN3wUIAXKZA9BZADJW2T1ZCUbCZC',
                },  
            },  
 }   







USE_LESS = False

logging.basicConfig(level=logging.DEBUG)



LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
                },
            'simple': {
                'format': '%(levelname)s %(message)s',
                },
            },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
                },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
                },
            },
        'loggers': {
            'django.request': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': False,
                },
            'django': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': True,
                },
            },
        }

FEED_IMPORT_TARGET_SITE = "http://omg.tt"
