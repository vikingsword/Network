# -*- coding: utf-8 -*-
import csv
import time
from selenium import webdriver
import pymysql


# # csv
# driver = webdriver.Edge()
#
# with open('./test.csv', 'a+', encoding='UTF-8') as f:
#     writer = csv.writer(f)
#
#     writer.writerow(["zs", "男", '18'])
#
#     f.close()
#
# time.sleep(3)
# driver.close()


# mysql

# 创建链接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider', charset='utf8')
# 创建游标
cursor = conn.cursor()
# 执行 sql
# effect_row = cursor.execute("insert into test values (1, 'zs', 19), (2, 'ls', 20)")
effect_row2 = cursor.executemany("insert into test(name,age) values (%s,%s)", [( 'zs', 19), ('ls', 20)])
# 提交
conn.commit()
# 关闭
cursor.close()
conn.close()


