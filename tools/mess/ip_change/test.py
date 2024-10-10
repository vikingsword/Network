# !usr/bin/env python
# -*- coding:utf-8 _*-
import requests

ip = "38.207.174.231"
port = "22"
url = f"https://www.toolsdaquan.com/toolapi/public/ipchecking2/{ip}/{port}"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'referer': 'https://www.toolsdaquan.com/ipcheck/'
}
print(url)
resp = requests.get(url, headers=headers)
print(resp.text)