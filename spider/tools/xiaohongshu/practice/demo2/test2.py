# !usr/bin/env python
# -*- coding:utf-8 _*-

def read_cookie():
    with open('cookie.txt', 'r') as f:
        return f.read()

print(read_cookie())