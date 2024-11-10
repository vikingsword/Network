# !usr/bin/env python
# -*- coding:utf-8 _*-

import smtplib
import ssl

EMAIL_ADD = 'vikingar01@163.com'
EMAIL_PASS = 'XCZbhsLDEGy8725h'

# 建立SMTP连接
smtp_server = 'smtp.163.com'
smtp_port = 465  # 465端口用于SSL加密
context = ssl.create_default_context()

# 使用SSL连接到SMTP服务器
smtp = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context)
smtp.login(EMAIL_ADD, EMAIL_PASS)

# 构建邮件内容
sender = EMAIL_ADD
receiver = 'receiver_email@example.com'  # 收件人地址需要填写实际的邮箱
subject = 'hello'
body = 'this is vikingar!'
msg = f'Subject: {subject}\n\n{body}'

# 发送邮件
smtp.sendmail(sender, receiver, msg)

# 关闭连接
smtp.quit()
