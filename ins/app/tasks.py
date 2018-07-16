from __future__ import absolute_import, unicode_literals


from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives


@shared_task
def send_email(subject, from_email, to, text_content, html_content=None):
    if not html_content:
        return send_mail(subject, text_content, from_email, to)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    return msg.send()
