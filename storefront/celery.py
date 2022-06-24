import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')
#os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

celery = Celery('storefron')
celery.config_from_object('django.conf:settings', namespace = 'CELERY')
celery.autodiscover_tasks()