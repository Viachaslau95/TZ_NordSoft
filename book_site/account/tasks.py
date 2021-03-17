from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from account.models import Account


@shared_task()
def send_password(account_id):
    user = Account.objects.get(pk=account_id)
    message = str(
        Account.objects.make_random_password(
            length=8,
            allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889"
        )
    )
    send_mail('Welcome', message, user.email, recipient_list=[user.email])
    user.set_password(message)
    user.save()
