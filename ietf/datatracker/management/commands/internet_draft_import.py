from django.core.management.base import BaseCommand
from django.core.mail import mail_admins

from ietf.datatracker.models import InternetDraft


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            InternetDraft.fetch_and_update()
        except Exception as e:
            mail_admins("IETF Datatracker %s import failed" % InternetDraft.__name__,
                        e.__repr__())
