# !usr/bin/env python
# -*- coding:utf-8 _*-
import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('x-ui.db')
cursor = conn.cursor()

# 测试插入
for i in range(2, 11):
    sql = 'INSERT INTO users2 (id,username, password) VALUES (?, ?, ?)'
    cursor.execute(sql, (i, 'Name_' + str(i), 'passwd_' + str(i)))

# 提交事务并关闭连接
conn.commit()
conn.close()
