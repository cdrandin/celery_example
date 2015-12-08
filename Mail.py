import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


class Mail(object):

    def __init__(self, login, password):
        super(Mail, self).__init__()
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.message = None
        self.server.starttls()
        self.server.login(login, password)
        self.from_addr = login

    def AddTextMessage(self, msgs=[], extension='html'):
        if self.message is None:
            self.__create_message()

        if msgs is not list:
            msgs = [msgs]

        self.message.attach(MIMEText(''.join(msgs), extension))

    def AddImageMessage(self, img_file_path):
        if self.message is None:
            self.__create_message()

        with open(img_file_path, 'rb') as infile:
            self.message.attach(MIMEImage(infile.read()))

    def AddMessageSubject(self, subject):
        if self.message is None:
            self.__create_message()

        self.message['Subject'] = subject

    def SendMessage(self, to, subject, msg):
        self.AddMessageSubject(subject)
        self.AddTextMessage(msg)
        return self.__Send(to)

    def SendImage(self, to, subject, img_file_path):
        self.AddMessageSubject(subject)
        self.AddImageMessage(img_file_path)
        return self.__Send(to)

    def SendSimpleMessage(self, to, msg):
        return self.SendMessage(to, '', msg)

    def SendSimpleImage(self, to, img_file_path):
        return self.SendImage(to, '', img_file_path)

    def ClearMessage(self):
        self.__create_message()

    def Quit(self):
        self.server.quit()

    def __Send(self, to, wipe=True):
        result = None
        if self.message is None:
            print 'Message has not been built'
            result = None
        else:
            self.message['From'] = self.from_addr
            self.message['To'] = to
            result = self.server.sendmail(
                self.from_addr, [to], self.message.as_string())

            # delete MIME Message
            if wipe:
                self.__create_message()

        return result

    def __create_message(self):
        self.message = MIMEMultipart()
