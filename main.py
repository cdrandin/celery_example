
from proj.tasks import *
import datetime


def main():
    in_1_min = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)

    res = send_email.apply_async(
        args=['cdrandin@hotmail.com', 'delayed message'], eta=in_1_min)

if __name__ == '__main__':
    main()
