import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mwx@&97%!$fx_*zgj(2ygi^(s=oh5j(cqb$=+-mkd9scbt!0v0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/login/'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'simple_pagination',
    'compressor',
    'common',
    'accounts',
    'cases',
    'contacts',
    'emails',
    'leads',
    'opportunity',
    'planner',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crm.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
###


###
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': '127.0.0.1',# change this to 'db' or your machine ip when developing using docker
        'PASSWORD': 'password',
        'PORT': 5432  # default postgres port
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 25
# AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', )


EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.getenv('SG_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('SG_PWD', '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
AUTH_USER_MODEL = 'common.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_FROM_EMAIL = 'no-reply@django-crm.micropyramid.com'
MAIL_SENDER = 'AMAZON'
INACTIVE_MAIL_SENDER = 'MANDRILL'

AM_ACCESS_KEY = os.getenv('AM_ACCESS_KEY', '')
AM_PASS_KEY = os.getenv('AM_PASS_KEY', '')
AWS_REGION = os.getenv('AWS_REGION', '')

MGUN_API_URL = os.getenv('MGUN_API_URL', '')
MGUN_API_KEY = os.getenv('MGUN_API_KEY', '')

SG_USER = os.getenv('SG_USER', '')
SG_PWD = os.getenv('SG_PWD', '')

MANDRILL_API_KEY = os.getenv('MANDRILL_API_KEY', '')

django_heroku.settings(locals())