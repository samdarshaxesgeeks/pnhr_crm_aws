import os
from decouple import config, Csv
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration





ENVIRONMENT = config("ENVIRONMENT")

if ENVIRONMENT == "heroku":
    sentry_sdk.init(
        dsn=config("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True
    )

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR=os.path.join(BASE_DIR,'static')
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'www.pnhrconsulting.com','pnhrconsulting.com', '172.31.12.102', 'ec2-3-111-148-181.ap-south-1.compute.amazonaws.com']


# ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

CRM_APPS = [
    'employees',
    'payroll',
    'leave',
    'organisation_details',
    'settings',
    'overtime',
    'holidays',
    'ems_auth',
    'ems_admin',
    'contract2',
    'notification',
    'cal',
    'invoice1',
    'crm_app',
    'contacts',
    # 'cont',
    'attendence',
    # 'attendance',

]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'javascript_settings',
    'crispy_forms',
    'django_crontab',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

INSTALLED_APPS = CRM_APPS + DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CRM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'CRM.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if DEBUG:

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.pnhr'),
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'crm',
        'USER': 'myprojectuser111',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'ems_auth.User'

AUTHENTICATION_BACKENDS = ['ems_auth.backends.EmailBackend']

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Kampala'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# AWS_ACCESS_KEY_ID = 'AKIASCMSXZU5632LPMUH'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'pnhr-crm-bucket'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_DEFAULT_ACL = 'public-read'
# AWS_LOCATION = 'static'




STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
#     ]

SENDGRID_API_KEY = config('SENDGRID_API_KEY')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")

MEDIA_ROOT = os.path.join(BASE_DIR, 'pics')
MEDIA_URL = 'pics/'

CRONJOBS = [
    ('0 0 * * *', 'overtime.cron.expire_overtime_applications'),  # Every day at Midnight
    ('0 0 * * *', 'leave.cron.expire_leave_plan_applications'),  # Every day at Midnight
    ('0 0 * * *', 'leave.cron.expire_leave_applications'),  # Every 1 minute
    ('0 3 * * 5', 'ems_admin.cron.delete_all_audit_trails'),  # Every 3 a.m on Friday
]
