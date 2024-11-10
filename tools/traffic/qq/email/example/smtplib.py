# !usr/bin/env python
# -*- coding:utf-8 _*-
import smtplib
import ssl

EMAIL_ADD = 'vikingar01@163.com'
EMAIL_PASS = 'XCZbhsLDEGy8725h'

# build smtp connect
smtp = smtplib.SMTP('smtp.163.com', 25)
context = ssl.create_default_context()
smtp = smtplib.SMTP_SSL('smtp.163.com', 465, context=context)
smtp.login(EMAIL_ADD, EMAIL_PASS)

# send email
sender = EMAIL_ADD
receiver = EMAIL_ADD
subject = 'hello'
body = 'this is vikingar! '
msg = f'Subject: {subject}\n\n{body}'
smtp.sendmail(sender, receiver, msg)

