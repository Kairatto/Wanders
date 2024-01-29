# __init__.py.py
from __future__ import absolute_import, unicode_literals

# Загружаем настройки celery при старте Django
from .celery import app as celery_app

__all__ = ('celery_app',)
