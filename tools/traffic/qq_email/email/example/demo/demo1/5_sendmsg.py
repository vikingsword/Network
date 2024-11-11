# !usr/bin/env python
# -*- coding:utf-8 _*-
# send message to many users
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
# to many users
msg['To'] = [EMAIL_SENDER, 'niemandea@163.com', 'abc@163.com']
msg.set_content(body)

# 一些邮件会保留最后的部分，上面不会显示，网易邮箱就是如此
msg.add_alternative('''\
<!DOCTYPE html>
<html>
<head>hello vikingar!</head>
<body>
    <h1 style="color: Red">Nice to meet you!</h1>
</body>
</html>
''', subtype='html')

# use with close smtp auto
with smtplib.SMTP_SSL('smtp.163.com', 465, context=context) as smtp:
    smtp.login(EMAIL_SENDER, EMAIL_PASS)
    # send message
    smtp.send_message(msg)
