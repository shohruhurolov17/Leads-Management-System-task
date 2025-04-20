from django.core.mail import send_mail, EmailMessage
from celery import shared_task
from typing import List
from environs import Env
from django.contrib.auth.models import User

env = Env()

env.read_env('.env')

EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')


@shared_task
def send_an_email(prospect_email: str, full_name: str) -> None:

    subject_prospect = 'Your submission has been received!'
    message_prospect = 'Thank you for your inquiry. Our team will contact you shortly.'

    send_mail(
        subject=subject_prospect,
        message=message_prospect,
        from_email=EMAIL_HOST_USER,
        recipient_list=[prospect_email],
        fail_silently=False,
    )

    attorney_emails = list(
        User.objects \
        .filter(groups__name='attorneys', email__isnull=False) \
        .values_list('email', flat=True)
    )

    subject_attorney = 'New Lead Submitted!'
    body_attorney = f"A new lead has been submitted:\n\nName: {full_name}\nEmail: {prospect_email}."

    send_mail(
        subject=subject_attorney,
        message=body_attorney,
        from_email=EMAIL_HOST_USER,
        recipient_list=attorney_emails,
        fail_silently=False,
    )

