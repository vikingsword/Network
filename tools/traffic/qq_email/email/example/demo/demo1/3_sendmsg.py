# !usr/bin/env python
# -*- coding:utf-8 _*-
# send message with file
import smtplib
import ssl
from email.message import EmailMessage

EMAIL_SENDER = 'vikingar01@163.com'
EMAIL_PASS = 'XCZbhsLDEGy8725h'

EMAIL_RECEIVER = '1974392477@qq.com'

# build smtp connect
smtp = smtplib.SMTP('smtp.163.com', 25)
context = ssl.create_default_context()

subject = 'hello'
body = 'hello vikingar! nice day2'
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = EMAIL_SENDER
msg['To'] = EMAIL_SENDER
msg.set_content(body)

filename = '1.jpg'
with open(filename, 'rb') as f:
    filedata = f.read()
msg.add_attachment(filedata, maintype='image', subtype='jpg', filename=filename)

# use with close smtp auto
with smtplib.SMTP_SSL('smtp.163.com', 465, context=context) as smtp:
    smtp.login(EMAIL_SENDER, EMAIL_PASS)
    # send message
    smtp.send_message(msg)
