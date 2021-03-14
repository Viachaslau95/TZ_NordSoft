import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_site.settings')

app = Celery('book_site')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.timezone = 'UTC'
