
# from proj.tasks import *

import os
import datetime


def main():
    filepath = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'file.txt')
    with open(filepath, 'a+') as outfile:
        outfile.write('[%s]: %s' % (datetime.datetime.now(), 'hello world!'))

    # in_1_min = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)

    # res = send_email.apply_async(
    #     args=['cdrandin@hotmail.com', 'delayed message'], eta=in_1_min)

if __name__ == '__main__':
    main()
