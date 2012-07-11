import django.dispatch

signal_ping = django.dispatch.Signal(providing_args=['ping_name', 'args', 'kwargs'])