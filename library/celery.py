from celery import Celery
import os
from django.core.mail import send_mail

# Настройки для celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')

app = Celery('library')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

