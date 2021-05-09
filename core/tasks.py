from celery import shared_task
from django.core.mail import send_mail
from time import sleep
from celery_send_email.settings import EMAIL_HOST_USER

@shared_task
def send_email_task(subject, message, recipient_list):
    from_email = EMAIL_HOST_USER
    send_mail(subject, message, from_email, recipient_list)
    #send_mail('test subject', 'test message', from_email, ['cidebeb172@goqoez.com'])
    return None
