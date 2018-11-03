import os
import CollegeWebsiteServer.settings.common as common

BASE_DIR = common.BASE_DIR
SECRET_KEY = common.SECRET_KEY
INSTALLED_APPS = common.INSTALLED_APPS
MIDDLEWARE = common.MIDDLEWARE
ROOT_URLCONF = common.ROOT_URLCONF
WSGI_APPLICATION = common.WSGI_APPLICATION
LANGUAGE_CODE = common.LANGUAGE_CODE
TIME_ZONE = common.TIME_ZONE
USE_I18N = common.USE_I18N
USE_L10N = common.USE_L10N
USE_TZ = common.USE_TZ

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'College_Website_Server/../templates')]
        ,
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'website',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '',
        'PORT': '5432',
    },
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'website',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '3306',
    },
}

DATABASE_ROUTERS = ['CollegeWebsiteServer.database_router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {
    # 'app1': 'db1',
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

STATIC_URL = '/templates/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/templates/static/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'templates/static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
