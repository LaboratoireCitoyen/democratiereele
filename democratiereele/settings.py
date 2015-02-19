"""
Django settings for democratiereele project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def project_directory(*join):
    return os.path.realpath(
        os.path.join(BASE_DIR, *join).replace('\\', '/'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't^$@)s00ff1teqn*5lahdj2o(8324yd0_)i-q4v#d5s)no4xb_'

THUMBNAIL_ALIASES = {
    '': {
        'rectangle_0': {
            'autocrop': True,
            'crop': 'smart',
            'size': (400, 300),
        },
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth', 
    'django.core.context_processors.debug', 
    'django.core.context_processors.i18n', 
    'django.core.context_processors.media', 
    'django.core.context_processors.static', 
    'django.core.context_processors.tz', 
    'django.core.context_processors.request', 
    'django.contrib.messages.context_processors.messages',
    'democratiereele.context_processors.no_form_tag',
    'account.context_processors.account',
)

PIPELINE_CSS = {
    'style': {
        'source_filenames': (
            'foundation/css/normalize.css',
            'foundation/css/foundation.css',
            'autocomplete_light/style.css',
            'fluent_comments/css/ajaxcomments.css',
            'font-awesome/css/font-awesome.css',
        ),
        'output_filename': 'css/style.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'script': {
        'source_filenames': (
            'autocomplete_light/autocomplete.js',
            'autocomplete_light/widget.js',
            'autocomplete_light/addanother.js',
            'autocomplete_light/text_widget.js',
            'autocomplete_light/remote.js',
            'fluent_comments/js/ajaxcomments.js',
            'respond/dest/respond.src.js',
            'modernizr/modernizr.js',
            'html5shiv/dist/html5shiv.js',
            'foundation/js/foundation.js',
        ),
        'output_filename': 'js/script.js',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = []

CITIES_LIGHT_INCLUDE_COUNTRIES = ['FR']
CITIES_LIGHT_TRANSLATION_LANGUAGES = ['fr']

BOWER_INSTALLED_APPS = (
    'jquery',
    'foundation',
    'html5shiv',
    'respond',
    'less',
    'font-awesome',
)


try:
    import raven
except ImportError:
    pass
else:
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)

ACCOUNT_ACTIVATION_DAYS = 7

STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.FileSystemFinder', 
   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
   'djangobower.finders.BowerFinder',
   'pipeline.finders.PipelineFinder',
)


# Application definition

INSTALLED_APPS = (
    'fluent_comments',
    'threadedcomments',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'project_specific',
    'django_gravatar',
    'django_markup',
    'djangobower',
    'pipeline',
    'taggit',
    'cities_light',
    'decision',
    'complaints',
    'crispy_forms',
    'crispy_forms_foundation',
    'autocomplete_light',
    'rules_light',
    'debug_toolbar',
    'easy_thumbnails',
    'account',
)

SITE_ID = 1
AUTHENTICATION_BACKENDS = ['django-dual-authentication.backends.DualAuthentication']

CRISPY_TEMPLATE_PACK = 'foundation-5'

FLUENT_COMMENTS_EXCLUDE_FIELDS = ('name', 'email', 'url', 'title')
COMMENTS_APP = 'project_specific'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
    'rules_light.middleware.Middleware',
)

ROOT_URLCONF = 'democratiereele.urls'

WSGI_APPLICATION = 'democratiereele.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'democratiereele',
    }
}

LANGUAGE_CODE = 'fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = project_directory('public/media')
MEDIA_URL = '/public/media/'
STATIC_ROOT = project_directory('public/static')
STATIC_URL = '/public/static/'
STATICFILES_DIRS = (project_directory('static'),)
TEMPLATE_DIRS = (project_directory('templates'),)
FIXTURE_DIRS = (project_directory('fixtures'),)
BOWER_COMPONENTS_ROOT = project_directory('bower')
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        },
        'cities_light': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        },
        'rules_light': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        }
    }
}


try:
    from local_settings import *
except ImportError:
    pass
