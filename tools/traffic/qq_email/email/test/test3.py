# !usr/bin/env python
# -*- coding:utf-8 _*-
EMAIL_RECEIVER = [_.strip() for _ in open('./users.txt', 'r', encoding='utf-8')]
for _ in EMAIL_RECEIVER:
    print(_)