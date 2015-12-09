from __future__ import absolute_import
from proj.celery import app
import datetime
import sys
sys.path.append("..")

from Mail import *


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


GMAIL_EMAIL = 'noreply.usahazmat@gmail.com'
GMAIL_PASSWORD = 'vEeryejcOvaBbyErdOonsyahogOOlARLPcX'
@app.task
def send_email(to_addr, msg):
    mail = Mail(GMAIL_EMAIL, GMAIL_PASSWORD)
    return mail.SendSimpleMessage(to_addr, msg)
