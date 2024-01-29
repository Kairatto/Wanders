from django.conf import settings
from config.celery import app
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# from celery import shared_task

User = get_user_model()

@app.task
def send_activation_code(email, activation_code):
    activation_link = f'http://http://127.0.0.1:8000/account/activate/{activation_code}/'
    html_message = render_to_string(
        'account/index.html',
        {'activation_link': activation_link}
        )

    send_mail(
        'Активируйте ваш аккаунт!',
        '',
        settings.EMAIL_HOST_USER,
        [email],
        html_message=html_message,
        fail_silently=False
    )

@app.task
def send_change_password_code(email, code):
    # try:
        html_message = render_to_string(
            'account/password_code_mail.html',
            {'code': code}
            )
        send_mail(
            'Сбросить пароль',
            '',
            settings.EMAIL_HOST_USER,
            [email],
            html_message=html_message,
            fail_silently=False   
        )
    # except ValidationError as e:
    #     print(f"Validation Error: {e}")
    # except Exception as e:
    #     print(f"An error occurred: {e}")


# @shared_task(name='check_activation')
def check_activation():               
    today = datetime.now(timezone.utc)
    for user in User.objects.filter(is_active=False) and ((today - user.created_at).seconds/3600) > 24:
        user.delete()