release: python manage.py migrate
web: gunicorn storefront.wsgi
worker: colery -a storefront worker