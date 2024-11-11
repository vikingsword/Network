# !usr/bin/env python
# -*- coding:utf-8 _*-
# send msg normal
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
body = 'hello vikingar! nice day'
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = EMAIL_SENDER
msg['To'] = EMAIL_SENDER
msg.set_content(body)

# use with close smtp auto
with smtplib.SMTP_SSL('smtp.163.com', 465, context=context) as smtp:
    smtp.login(EMAIL_SENDER, EMAIL_PASS)
    # send message
    smtp.send_message(msg)
