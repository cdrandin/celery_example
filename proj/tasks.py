from __future__ import absolute_import
from proj.celery import app
import datetime
import sys
sys.path.append("..")

from gmail import GMail
from gmail import Message


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def writeDatetimeNow(msg):
    with open('file.txt', 'a+') as outfile:
        outfile.write(str(datetime.datetime.now()))

GMAIL_EMAIL = 'noreply.usahazmat@gmail.com'
GMAIL_PASSWORD = 'vEeryejcOvaBbyErdOonsyahogOOlARLPcX'


@app.task
def send_email(to_addr, subject, msg):
    mail = GMail(GMAIL_EMAIL, GMAIL_PASSWORD)
    mail.connect()

    if to_addr is list:
        to_addr = ', '.join(list(to_addr))

    mail.send(Message(subject, to=to_addr, html=msg))
    mail.close()

