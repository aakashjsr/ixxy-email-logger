from admin_tools.dashboard import modules
from django.core.urlresolvers import reverse

from .models import EmailLog

def get_status_message():
    failed_emails = EmailLog.objects.filter(success=False)
    if failed_emails:
        count = failed_emails.count()
        plural = "s" if count > 1 else ""
        return (
            "<span style='color: red;'>{} failed email{}.</span><br>"
            "<a href='{}'>View/fix failed email{}</a>".format(
                count,
                plural,
                reverse('admin:email_logger_emaillog_changelist') + '?success_exact=0',
                plural,
            )
        )
    else:
        return ''

email_logger_dashboard_module = modules.LinkList(
    title="Failed Emails",
    pre_content=get_status_message,
)
