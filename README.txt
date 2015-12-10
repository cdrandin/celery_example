For Windows server:

Start up Redis server
“C:\Program Files\Redis\redis-server.exe”

Start up Celery project tasks
dir “C:\Users\ServerAdmin\Documents\celery_example”

// foreground
celery -A proj worker -l info --pool=solo

// background
celery multi start w1 -A proj -l info --pool=solo

Now task queue is ready.

For Linux :
don’t forget virtual env if any.

Start up Redis server
redis-server

Start up Celery project tasks
cd /Users/cdrandin/Programming/Python/celery_example

// foreground
celery -A proj worker -l info

// background
celery multi start w1 -A proj -l info


Resources:
https://github.com/celery/celery/issues/2146