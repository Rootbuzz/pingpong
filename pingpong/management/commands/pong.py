from django.conf import settings
from django.core.management.base import BaseCommand
from pingpong.utils import send_ping

class Command(BaseCommand):

    def handle(self, ping_name, *args, **kwargs):
        send_ping(ping_name, *args, **kwargs)
