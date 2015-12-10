from __future__ import absolute_import
from celery import Celery
from celery.schedules import crontab
import datetime

app = Celery('proj',
             broker='redis://',
             backend='redis://',
             include=['proj.tasks'])

app.config_from_object('proj')

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    # CELERY_TASK_SERIALIZER='json',
    # CELERY_ACCEPT_CONTENT=['json'],
    CELERY_ENABLE_UTC = True,
    CELERY_TIMEZONE = 'US/Pacific',

    CELERYBEAT_SCHEDULE = {
        'mul_every_min': {
            'task': 'proj.tasks.mul',
            'schedule': datetime.timedelta(seconds=30), # crontab(minute='*'), # Execute every minute.
            'args': (2, 3),
            # 'args': ('cdrandin@hotmail.com', str(datetime.datetime.now())),
        },
    }
)

if __name__ == '__main__':
    app.start()

# get celerybeat to work 
# celery -A proj worker -B -l info

# or use celery -A proj beat
# to setup scheduler

# then celery worker -A proj -l info
# will process any queued task from the scheduler