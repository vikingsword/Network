# !usr/bin/env python
# -*- coding:utf-8 _*-
import requests
url = "https://ipdb.api.030101.xyz/?type=bestproxy"
resp = requests.get(url=url).text.strip()
arr = resp.split("\n")
print(arr)
for item in resp.split('\n'):
    print(item)

