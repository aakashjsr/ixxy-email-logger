from django.contrib import admin

from email_logger.models import EmailLog

class EmailLogAdmin(admin.ModelAdmin):
    name = 'Website Content'
    list_display = ('label', 'subject', 'sender', 'recipients', 'created')
    search_fields = ('label', 'subject')

admin.site.register(EmailLog, EmailLogAdmin)