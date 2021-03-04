from __future__ import absolute_import, unicode_literals

from book_site.celery import app


@app.task
def my_first_task():
    print('Первое')


@app.task
def my_second_task():
    print('Второе')
