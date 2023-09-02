from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email(user, subject, template_name, context):
    """Sends an email to the user."""

    body = render_to_string(template_name, context)

    send_mail(subject, '', settings.EMAIL_HOST_USER, [user.email], html_message=body, fail_silently=False)

# def send_email(user, welcome_text):
#     """Sends an email to the user."""

#     email_subject = 'Welcome to our website!'
#     email_body = welcome_text

#     send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

