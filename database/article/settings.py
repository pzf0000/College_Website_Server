import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WSGI_APPLICATION = 'easy.database.wsgi.application'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'article',
    #     'USER': 'postgres',
    #     'PASSWORD': 'postgres',
    #     'HOST': '',
    #     'PORT': '5432',
    # },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

from easy.database.settings import *

INSTALLED_APPS += [
    'models',
]
