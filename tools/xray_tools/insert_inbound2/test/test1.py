# !usr/bin/env python
# -*- coding:utf-8 _*-
import random
import string

def generate_random_string(length):
    """生成指定长度的随机字符串，只包含小写字母和数字"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_uuid():
    """生成符合 8+4+4+4+12 格式的字符串"""
    parts = [
        generate_random_string(8),
        generate_random_string(4),
        generate_random_string(4),
        generate_random_string(4),
        generate_random_string(12)
    ]
    return "-".join(parts)

if __name__ == '__main__':
    print(generate_uuid())