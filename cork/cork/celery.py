import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cork.settings")

#  celery -A cork worker --loglevel=info -P gevent --concurrency 1 -E
app = Celery("cork")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
