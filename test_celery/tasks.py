# Create your tasks here

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from datetime import timedelta



@periodic_task(run_every=(timedelta(seconds=5)))
def say():
    print('hello')