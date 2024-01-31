from random import random

import requests

# 这个网址 需要 模拟登陆

url = 'http://www.5jwl.com/user/checkusername.asp'

headers = {
    'Host': 'www.5jwl.com',
    'Content-Length': '80',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.5jwl.com',
    'Referer': 'http://www.5jwl.com/user/register2.asp',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': '__yjs_duid=1_fc95c82500c34271bfe9645ac0f959ae1690705139477; ASPSESSIONIDSCSCBBSQ=CMPBIJPCHHMAHBCNCBOMKDJH',
    'Connection': 'close'
}
random_r = random.random()
data = {
    'step': 'getverifycode',
    'mobi': '17758830796',
    'vcode': 'HexFMvozd6',
    'ajax': '1',
    'r': '0.8130732411537946'
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)


