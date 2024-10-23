# !usr/bin/env python
# -*- coding:utf-8 _*-
import random
import string

# 生成包含字母和数字的字符池
characters = string.ascii_letters + string.digits

# 使用random.choices从字符池中随机选择42个字符并组成字符串
random_password = ''.join(random.choices(characters, k=42))

print("随机生成的42位密码：", random_password)
