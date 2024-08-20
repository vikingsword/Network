# !usr/bin/env python
# -*- coding:utf-8 _*-

with open("cookie.txt", "r") as f:
    res = f.read()
    cookies = res.split(";")
    for cookie in cookies:
        print(cookie.strip())

print('---------------------')

with open("cookie2.txt", "r") as f:
    res = f.read()
    cookies = res.split(";")
    for cookie in cookies:
        print(cookie.strip())

