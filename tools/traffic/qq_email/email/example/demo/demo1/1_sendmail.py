# !usr/bin/env python
# -*- coding:utf-8 _*-
# send email by smtplib
import smtplib
import ssl

EMAIL_SENDER = 'vikingar01@163.com'
EMAIL_PASS = 'XCZbhsLDEGy8725h'

EMAIL_RECEIVER = '1974392477@qq.com'

# build smtp connect
smtp = smtplib.SMTP('smtp.163.com', 25)
context = ssl.create_default_context()

# use with close smtp auto
with smtplib.SMTP_SSL('smtp.163.com', 465, context=context) as smtp:
    smtp.login(EMAIL_SENDER, EMAIL_PASS)
    # send email
    sender = EMAIL_SENDER
    receiver = 'kaceb94153@opposir.com'
    subject = 'hello'
    body = 'this is vikingar! hello niemandea'
    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(sender, receiver, msg)
