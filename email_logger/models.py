from datetime import datetime

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

def log_mail(label, subject, text, sender, recipients, html='', cc=[], bcc=[], headers={}):
    email_log = EmailLog(
        label = label, 
        subject = subject, 
        sender = sender, 
        recipients = ','.join(recipients), 
        text = text, 
        html = html, 
        cc = ','.join(cc), 
        bcc = ','.join(bcc), 
        headers = unicode(headers), 
    )
    email_log.save()

