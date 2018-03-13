from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

app=Celery('plugcrm')
app.config_from_object('plugcrm.celeryconfig')
app.autodiscover_tasks()

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plugcrm.settings')
#
# if __name__ == '__main__':
#     app.start()