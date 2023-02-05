import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import global_value as g

class MailSender:
    def send(self, to_address, subject, message):
        message_object = self.create_message(g.FROM_ADDRESS, to_address, subject, message)
        self.execute(to_address, message_object)

    def execute(self, to_address, message):
        print(g.SMTP_HOST)
        print(g.SMTP_PORT)
        print(g.FROM_ADDRESS)
        print(g.FROM_ADDRESS_PASSWORD)
        smtpobj = smtplib.SMTP(g.SMTP_HOST, g.SMTP_PORT)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(g.FROM_ADDRESS, g.FROM_ADDRESS_PASSWORD)
        smtpobj.sendmail(g.FROM_ADDRESS, to_address, message.as_string())
        smtpobj.close()

    def create_message(self, from_address, to_address, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = from_address
        msg['To'] = to_address
        # msg['Bcc'] = bcc_addrs
        msg['Date'] = formatdate()
        return msg

    
