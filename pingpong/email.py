from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def render_to_email(template, cx, recipients, send_from=None, **kwargs):
    if send_from is None:
        send_from = settings.DEFAULT_FROM_EMAIL
    
    # it probably do what you expect if recipients is a string
    if isinstance(recipients, basestring):
        raise Exception("recipients is generally a list or tuple... definitely not a string")
    
    rendered = render_to_string(template, cx)
    rendered = rendered.strip()
    
    if "\n" in rendered:
        subject, message = rendered.split("\n", 1)
    else:
        subject, message = rendered, ''
        
    message = message.strip()
    
    send_mail(subject, message, send_from, recipients, **kwargs)