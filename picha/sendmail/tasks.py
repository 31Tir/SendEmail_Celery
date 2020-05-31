from celery import shared_task
from django.core.mail import send_mail
from picha.settings import EMAIL_HOST_USER


from django.utils.html import strip_tags
from django.conf import settings
from django.template import loader


@shared_task
def email(sub, text, users ):
    html_message = loader.render_to_string('post.html',{})
    result = send_mail( subject=sub, message=text, from_email=EMAIL_HOST_USER, recipient_list=users , fail_silently = False, html_message = html_message )
    return result



