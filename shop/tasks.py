from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


@shared_task
def send_email(user, subject, template_name, context):
    """Sends an email to the user."""

    body = render_to_string(template_name, context)

    send_mail(subject, '', settings.EMAIL_HOST_USER, [user.email], html_message=body, fail_silently=False)
