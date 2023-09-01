from django.conf import settings
from django.core.mail import send_mail


def send_email(user, welcome_text):
    """Sends an email to the user."""

    email_subject = 'Welcome to our website!'
    email_body = welcome_text

    send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
