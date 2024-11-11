# !usr/bin/env python
# -*- coding:utf-8 _*-
# send from 163 to many qq users
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import yaml

# 发送方和接收方邮件地址
with open('./config.yml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
sender_email = config['EMAIL']['SENDER']
sender_password = config['EMAIL']['KEY']

# 163邮箱的SMTP服务器和端口
smtp_server = config['EMAIL']['SERVER']
smtp_port = config['EMAIL']['PORT']

receiver_email = [_.strip() for _ in open('./users.txt', 'r', encoding='utf-8')]

# 邮件内容
subject = 'Test email'
body = 'hello niemandea'


# 创建邮件内容
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# 连接到163 SMTP服务器并发送邮件
try:
    with SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)  # 登录到163邮箱
        server.send_message(msg)  # 发送邮件
    print("email sent successfully")
except Exception as e:
    print(f"email send failed: {e}")
