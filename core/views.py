from django.shortcuts import render, redirect

from .tasks import send_email_task

def index(req):
    return render(req,'send_email.html')

def send_email_view(req):
    emails = list(req.POST.get('emails').split(','))
    subject = req.POST.get('subject')
    message = req.POST.get('message')
    send_email_task.delay(subject, message, emails)
    return redirect(index)
