import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_site.settings')

app = Celery('book_site')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'first_task': {
        'task': 'account.tasks.my_first_task',
        'schedule': 10.0,
    },
    'second_task': {
        'task': 'account.tasks.my_second_task',
        'schedule': 25.0,
    },
}
app.conf.timezone = 'UTC'
