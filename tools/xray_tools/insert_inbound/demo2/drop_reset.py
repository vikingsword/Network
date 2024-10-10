# !usr/bin/env python
# -*- coding:utf-8 _*-
import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('x-ui.db')
cursor = conn.cursor()

# 删除表（如果存在）
cursor.execute("DROP TABLE IF EXISTS inbounds")

table_data = '''
    CREATE TABLE "inbounds" (
      "id" integer PRIMARY KEY AUTOINCREMENT,
      "user_id" integer,
      "up" integer,
      "down" integer,
      "total" integer,
      "remark" text,
      "enable" numeric,
      "expiry_time" integer,
      "listen" text,
      "port" integer,
      "protocol" text,
      "settings" text,
      "stream_settings" text,
      "tag" text,
      "sniffing" text,
      CONSTRAINT "uni_inbounds_tag" UNIQUE ("tag" ASC)
    );
'''

# 重新创建表
cursor.execute(table_data)

# 提交更改并关闭连接
conn.commit()
conn.close()

print("Table 'inbounds' has been recreated successfully.")
