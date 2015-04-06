from datetime import datetime
import json

from django.db import models

class EmailLog(models.Model):
    label = models.CharField(max_length=128)
    subject = models.CharField(max_length=256)
    sender = models.CharField(max_length=256)
    recipients = models.TextField()
    text = models.TextField(blank=True)
    html = models.TextField(blank=True)
    cc = models.TextField(blank=True)
    bcc = models.TextField(blank=True)
    created = models.DateTimeField(default=datetime.now)
    headers = models.TextField(blank=True)


def log_emails(label, emails):
    for email in emails:
        EmailLog.objects.create(
            label=label,
            subject=email.subject,
            sender=email.from_email,
            recipients=', '.join(email.to),
            text=email.body,
            html=getattr(email, 'alternatives', '') and email.alternatives[0][0], # TODO handle multiple alternatives?
            cc=','.join(email.cc),
            bcc=','.join(email.bcc),
            headers=json.dumps(email.extra_headers),
        )

