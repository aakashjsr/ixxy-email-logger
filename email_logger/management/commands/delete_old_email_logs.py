from datetime import timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from email_logger.models import EmailLog


class Command(BaseCommand):

    def handle(self, *args, **options):
        now = timezone.now()
        if getattr(settings, 'AUTO_DELETE_OLD_EMAILLOG_RENTATION_DAYS', None):
            retention_time = now - timedelta(days=settings.AUTO_DELETE_OLD_EMAILLOG_RENTATION_DAYS)
        else:
            two_years_ago = now - timedelta(days=365*2)
            retention_time = two_years_ago
        logs_to_delete = EmailLog.objects.filter(created__lte=retention_time)
        print(
            '{} Email Logs to delete. We have {} email logs in total. '.format(
                logs_to_delete.count(), EmailLog.objects.all().count()
            )
        )
        logs_to_delete.delete()
