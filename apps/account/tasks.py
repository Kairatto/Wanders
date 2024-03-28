from django.conf import settings
from config.celery import app
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()

@app.task
def send_activation_code(email, activation_code):
    activation_link = f'http://127.0.0.1:8000/account/activate/{activation_code}/'
    html_message = render_to_string(
        'account/code_mail.html',
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


@app.task
def check_activation():
    threshold = now() - timedelta(hours=24)
    users_to_delete = User.objects.filter(is_active=False, created_at__lt=threshold)
    users_to_delete.delete()
