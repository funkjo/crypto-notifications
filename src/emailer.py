from dotenv import load_dotenv
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

gmail_pass = os.getenv('GMAIL_PASS')
port = 465


class Emailer:
    def __init__(self):
        self.sender_email = 'crypto.alerts.jf@gmail.com'
        self.receiver_email = 'funkjo00@gmail.com'
        self.port = 465

    def create_message(self, _asset, _open, _close, _pct_change, _type):
        
        message = MIMEMultipart('alternative')
        message['From'] = self.sender_email
        message['To'] = self.receiver_email
        
        if _type == 'hourly':
            message['Subject'] = _asset + ' changed by ' + _pct_change + ' percent in the last hour!'
            text = """
            {asset} changed by {pct_change} percent in the last hour!\n
            Open price: ${open}\n
            Close price: ${close}\n
            Pct. Change: {pct_change} percent\n
            """.format(asset=_asset, pct_change=_pct_change, open=_open, close=_close)
            email_body = MIMEText(text, 'plain')
            message.attach(email_body)
            
        return message

    def send_email(self, _asset, _open, _close, _pct_change, _type):
        context = ssl.create_default_context()
        message = self.create_message(_asset, str(_open), str(_close), str(_pct_change), _type)
        with smtplib.SMTP_SSL('smtp.gmail.com', self.port, context=context) as server:
            server.login('crypto.alerts.jf@gmail.com', gmail_pass)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())


emailer = Emailer()
emailer.send_email('ADA', 2.85, 2.90, 5.00, 'hourly')




