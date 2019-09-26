from django_cron import cronScheduler
from django_cron import Job
from django.core.management import call_command

from django_cron import HOUR, DAY, WEEK


class RunDeleteOldEmailLogs(Job):
    
    run_every = WEEK
    
    def job(self):
        call_command(
            "delete_old_email_logs",
        )

cronScheduler.register(RunDeleteOldEmailLogs)
