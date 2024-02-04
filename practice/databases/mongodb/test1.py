# !usr/bin/env python
# -*- coding:utf-8 _*-

import pymongo

# 连接到MongoDB数据库
client = pymongo.MongoClient("mongodb://localhost:27017/")  # 请根据实际情况修改连接字符串

# 选择或创建数据库
mydb = client["mydatabase"]

# 选择或创建集合（表）
mycollection = mydb["mycollection"]

# 插入文档
data = {"name": "John", "age": 30, "city": "New York"}
result = mycollection.insert_one(data)
print(f"Inserted document ID: {result.inserted_id}")

# 查询文档
query = {"name": "John"}
document = mycollection.find_one(query)
print(f"Query result: {document}")

# # 更新文档
# update_query = {"name": "John"}
# update_data = {"$set": {"age": 31}}
# mycollection.update_one(update_query, update_data)
# print("Document updated")
#
# # 查询更新后的文档
# updated_document = mycollection.find_one(update_query)
# print(f"Updated document: {updated_document}")
#
# # 删除文档
# delete_query = {"name": "John"}
# mycollection.delete_one(delete_query)
# print("Document deleted")

# 关闭连接
client.close()
