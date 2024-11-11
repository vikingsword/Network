from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 发送方和接收方邮件地址
sender_email = 'vikingar01@163.com'  # 发件人的163邮箱地址
receiver_email = '1974392477@qq.com'  # 收件人的QQ邮箱地址

# 163邮箱的SMTP服务器和端口
smtp_server = 'smtp.163.com'
smtp_port = 465  # 使用SSL加密
smtp_password = 'XCZbhsLDEGy8725h'  # 163邮箱的密码（或者授权码）

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
        server.login(sender_email, smtp_password)  # 登录到163邮箱
        server.send_message(msg)  # 发送邮件
    print("邮件发送成功")
except Exception as e:
    print(f"邮件发送失败: {e}")
