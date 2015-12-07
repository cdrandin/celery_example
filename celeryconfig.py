BROKER_URL = 'redis://'
CELERY_RESULT_BACKEND = 'redis://'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'US/Pacific'
CELERY_ENABLE_UTC = True

# CELERY_ROUTES = {
#     'tasks.add': 'low-priority',
# }

# CELERY_ANNOTATIONS = {
#     'tasks.add': {'rate_limit': '10/m'}
# }
