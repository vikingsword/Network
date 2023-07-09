import socket
import time

import requests


# 子域名查询
def getIpByHost(url):
    res = socket.gethostbyname(url)
    return res


# 1. 利用字典加载爆破进行查询
for o in open('E:\Sec\Tools\字典\\fuzzDicts\directoryDicts\php\phpFileName.txt'):
    url = 'www.xiaodi8.com/' + o
    try:
        ip = getIpByHost(url)
        print(url + '    ' + ip)
        time.sleep(0.1)

    except Exception as e:
        pass
# 2. 利用bing或第三方接口进行查询
