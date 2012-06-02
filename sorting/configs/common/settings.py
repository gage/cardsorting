import django
import os
import django.conf.global_settings as DEFAULT_SETTINGS

#aliases
dirname = lambda path: os.path.dirname(path)
realpath = lambda filep: os.path.realpath(filep)

# SITE_ROOT: "../.."
SITE_ROOT = dirname(dirname(dirname(realpath(__file__))))
SITE_DOMAIN = ""

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
        # ('Your Name', 'your_email@example.com'),
        )

MANAGERS = ADMINS

DATABASES = {
        'default': {
            'ENGINE': 'dbindexer',
            'TARGET': 'mongodb',
            'NAME': 'sorting',
            'TEST_NAME': 'test_sorting',
            },
        'mongodb': {
            'ENGINE': 'django_mongodb_engine',
            'NAME': 'sorting',
            'POST': 8000,
            'TEST_NAME': 'test_sorting',
            },
        }



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Taipei'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'


LANG_ZH = 0
LANG_JP = 1
LANG_EN = 2

LANG_CHOICES = [
        (LANG_ZH, "ZH"),
        (LANG_JP, "JP"),
        (LANG_EN, "EN"),        
        ]      


#SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

GLOBALS_STATIC_ROOT = os.path.join(SITE_ROOT, 'apps/globals/static')
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
        )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'httppjlci7^3hmy2rz88f5=38x0fz59v&yzitai4h5p86s*0dy'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
        #'django.template.loaders.filesystem.Loader',
        #'django.template.loaders.app_directories.Loader',
        #     'django.template.loaders.eggs.Loader',
        'coffin.template.loaders.Loader',
        )

JINJA2_TEMPLATE_LOADERS = (
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.filesystem.Loader',
        )

JINJA2_DISABLED_APPS = (
        'admin',
        )

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
        )

MIDDLEWARE_CLASSES = (
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.http.ConditionalGetMiddleware',
        'globals.middleware.MobileDetectMiddleware',
        #'debug_toolbar.middleware.DebugToolbarMiddleware',
        )

ROOT_URLCONF = 'sorting.configs.common.urls'

TEMPLATE_DIRS = (
        os.path.join(SITE_ROOT, 'templates'),
        #os.path.join(SITE_ROOT, 'lib/debug_toolbar/templates'),
        )


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
                }
            },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
                },
            }
        }

LOCALE_PATHS = (
        os.path.join(SITE_ROOT, 'locale'),
        )




INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'django.contrib.admin',
        'django.contrib.admindocs',

        'django_mongodb_engine',
        'djangotoolbox',
        'dbindexer',
        'imagekit',
        'piston',
        #'debug_toolbar',
        )

SITE_APPS = (
        'globals',
        )

INSTALLED_APPS += SITE_APPS

#AUTHENTICATION_BACKENDS = ()

LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = "/logged_in"


## HAYSTACK

## MongoDB
MONGODB_AUTOMATIC_REFERENCING = True

## DummyCaching ( for development, doesn't do anything )
"""
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
"""

## less
USE_LESS = True

DOWNLOAD_DIRECTORY = '/tmp/'



APPEND_SLASH = True

#FACEBOOK_USER_ID = "100000503406934"
#FACEBOOK_ACCESS_TOKEN = "AAACcZBR25o3ABAAmlWa1jzQas4HFWIJjDISnlTv7CaqogCrydMwpaFZCCmNuhTHZCVI39TkAcDduUPQiKrRR2PMkZA3NtrktoweS0RwhrgZDZD"


#=========================
# Redbug's test account
#=========================

# page owner's access token has no limits of post per day
#FACEBOOK_PAGE_OWNER_ACCESS_TOKEN ="AAACcZBR25o3ABAEE8QYZB5YmuCtgWZBUZAYuxZB35Y2rKGSxDIJySQMrxZAaCbKZArYHqZBONtkTqNwtmmct0VzHCV64xej2qN3wUIAXKZA9BZADJW2T1ZCUbCZC"


#DJANGO DEBUG BAR
#HIDE_DJANGO_SQL = True

"""
DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        #'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
        )
"""


# Allow for local overriding
try:
    from settings_local import *
except ImportError:
    pass

