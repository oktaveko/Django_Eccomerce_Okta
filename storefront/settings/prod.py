import os
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['django-eccomerce-okta.herokuapp.com']

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DB_NAME"),
        'USER' : os.environ.get("DB_USER"),
        'PASSWORD':os.environ.get("DB_PASS"),
        'HOST' :os.environ.get("DB_HOST"),
        'PORT' : '3306',
    }
}

REDIS_URL = os.environ.get('REDIS_URL')

CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "TIMEOUT" : 10 * 60, 
        "OPTIONS": {
            'PASSWORD': os.environ.get('REDIS_PASS'),
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 465

