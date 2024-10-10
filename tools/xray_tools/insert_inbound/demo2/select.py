# !usr/bin/env python
# -*- coding:utf-8 _*-
import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('x-ui.db')
cursor = conn.cursor()

# 测试查询
for i in range(1, 20):
    cursor.execute("SELECT * FROM inbounds2 where id = ?", (i,))
    result = cursor.fetchone()

    if result:
        print(f"Result for id {i}: {result}")
    else:
        print(f"No result found for id {i}")


# 提交事务并关闭连接
# conn.commit()
conn.close()
