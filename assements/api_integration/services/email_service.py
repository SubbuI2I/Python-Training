from django.core.mail import send_mail
from django.template.loader import render_to_string

from assements import settings
from logger.log import Log


class EmailService:
    def mail_notify(self, subject, message='This is mail body', recipients_mails=[]):
        log = Log()
        try:
            log.write_log('This is from email service', 20)
            email_body = render_to_string(
                'api_integration/includes/email_template.html', {'content': message, 'user': 'User'})
            send_mail(subject=subject,
                      message='Test Mail Template',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=recipients_mails,
                      fail_silently=False,
                      auth_user=settings.EMAIL_HOST_USER,
                      auth_password=settings.EMAIL_HOST_PASSWORD,
                      html_message=email_body)
            log.write_log('Mail Sent Successfully to {recipients_mails}', 10)
        except Exception as ex:
            log.write_log(ex, loglevel=40)
            return ex
