# !usr/bin/env python
# -*- coding:utf-8 _*-
from pathlib import Path

# 创建一个路径对象
path = Path('.//to//file.txt')

# 检查路径是否存在
if path.exists():
    print("文件存在")

# 获取文件名
print("文件名:", path.name)

# 获取文件后缀
print("文件后缀:", path.suffix)

# 获取文件父目录
print("父目录:", path.parent)

# 创建目录
path.parent.mkdir(parents=True, exist_ok=True)

# 读取文件内容
content = path.read_text()
print("文件内容:", content)
