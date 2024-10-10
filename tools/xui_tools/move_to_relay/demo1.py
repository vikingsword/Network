# !usr/bin/env python
# -*- coding:utf-8 _*-
import os
import sqlite3
import json

conn = sqlite3.connect('x-ui.db')
cursor = conn.cursor()
# 测试插入

sql = (
    'SELECT port, remark from inbounds'
)
res = cursor.execute(sql)
domain = "prod0.vikingsword.top"
output_str = ""
cou = 0
if os.path.exists('res.txt'):
    os.remove('res.txt')

with open('res.txt', 'a+') as f:
    for row in res:
        port = str(row[0])
        name = str(row[1])
        # 构建字典
        output_dict = {
            "dest": [f"{domain}:{port}"],
            "listen_port": int(port),
            "name": name
        }
        cou += 1

        # 输出 JSON 格式字符串
        output_str = json.dumps(output_dict, ensure_ascii=False)
        res = output_str.replace(" ", "")
        f.write(res + "\n")
        print(res)

print(cou)
# 提交事务并关闭连接
conn.commit()
conn.close()
