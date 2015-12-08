from __future__ import absolute_import

from proj.celery import app


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
def send_email(frm, to, msg):
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)

    #Next, log in to the server
    server.login("cdrandin@gmail.com", "4:Zpb6H]fAs6y43H<Z]W7xVw")

    #Send the mail
    server.sendmail(frm, to, msg)