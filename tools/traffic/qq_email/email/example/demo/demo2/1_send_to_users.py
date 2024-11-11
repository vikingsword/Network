# !usr/bin/env python
# -*- coding:utf-8 _*-
# send msg normal
import smtplib
import ssl
from email.message import EmailMessage
import yaml

# load sender information
with open('./config.yaml') as f:
    config = yaml.safe_load(f)
EMAIL_SENDER = config['EMAIL']['SENDER']
EMAIL_PASS = config['EMAIL']['KEY']

EMAIL_RECEIVER = [line.strip() for line in open('./users.txt', 'r')]

# build smtp connect
smtp = smtplib.SMTP('smtp.163.com', 25)
context = ssl.create_default_context()

subject = 'hello'
body = 'hello vikingar! nice day'
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = EMAIL_SENDER
msg['To'] = EMAIL_RECEIVER
msg.set_content(body)

# use with close smtp auto
with smtplib.SMTP_SSL('smtp.163.com', 465, context=context) as smtp:
    smtp.login(EMAIL_SENDER, EMAIL_PASS)
    # send message
    smtp.send_message(msg)
