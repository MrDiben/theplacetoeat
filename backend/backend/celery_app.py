import os
import time

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")


app = Celery("backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    time.sleep(10)
    print("Task is done")
