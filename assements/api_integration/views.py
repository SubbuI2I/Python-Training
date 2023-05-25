from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from config import Configurations
from logger.log import Log
from api_integration.services.email_service import EmailService


def index(request):
    config_details = Configurations.logging_display(request)

    # region For Learning
    # server_name = Configurations.server_name
    # server_ip = Configurations.server_ip  # Read from class properties
    # size = config_details['size']  # Read from class method
    # logging.log(1, f" {config_details} '-' {server_ip} '->' {server_name} {size}")
    # endregion

    # region Logging
    # formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    # logger = logging.getLogger('file_logger')
    # file_handler = logging.FileHandler('debug.log')
    # file_handler.setLevel(logging.DEBUG)
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)

    # timed_handler = TimedRotatingFileHandler(
    #     'logger/log_files/timed.log', when='m', interval=1, backupCount=2)
    # timed_handler.setFormatter(formatter)
    # timed_handler.setLevel(logging.ERROR)
    # logger.addHandler(timed_handler)
    # endregion
    log = Log()
    # region Email Config with Templates
    msg = 'Success'
    # for temporary testing used below mail
    recipients_mails = ['vinitha.ravichandran@ideas2it.com']
    try:
        EmailService.mail_notify(request, subject='Email Notification',
                                 message='This is test email', recipients_mails=recipients_mails)
        log.write_log('email sent successfully using EmailService ')

        # send mail also using below methods
        # send_mail(subject='message', message='Test message', from_email=settings.EMAIL_HOST_USER,
        #           recipient_list=recipients_mails, fail_silently=False,
        #           auth_user=settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD)

        # another approach to send mail with attachments
        email_subject = 'Test Mail Notification'
        email_body = render_to_string(
            'api_integration/includes/email_template.html', {'content': 'This is mail content', 'user': 'User'})
        from_email = 'subramanian.palaniappan@ideas2it.com'
        email = EmailMessage(subject=email_subject, body=email_body, from_email=from_email,
                             to=recipients_mails)
        email.content_subtype = 'html'  # Set the content type to HTML
        email.attach_file('api_integration/static/images/logo.jpg',
                          mimetype='image/jpg')
        email.send()

    except Exception as ex:
        msg = 'Error'
        log.write_log(f'Error in sending email { str(ex) }')
    # endregion

    return render(request, 'api_integration/index.html', {'config': config_details, 'msg': msg})
