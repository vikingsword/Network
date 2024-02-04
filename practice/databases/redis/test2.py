# !usr/bin/env python
# -*- coding:utf-8 _*-
import redis

# 连接到本地Redis服务器，默认端口是6379
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# 设置键值对
redis_client.set('my_key', 'Hello, Redis!')

# 获取键对应的值
value = redis_client.get('my_key')
print(value.decode('utf-8'))

# 增加一个值
redis_client.incr('counter')

# 获取增加后的值
counter_value = redis_client.get('counter')
print(counter_value.decode('utf-8'))

# 存储和获取列表
redis_client.rpush('my_list', 'item1')
redis_client.rpush('my_list', 'item2')

# 获取列表的所有元素
my_list = redis_client.lrange('my_list', 0, -1)
print([item.decode('utf-8') for item in my_list])

# 存储和获取哈希表
redis_client.hset('my_hash', 'field1', 'value1')
redis_client.hset('my_hash', 'field2', 'value2')

# 获取哈希表的所有字段和值
my_hash = redis_client.hgetall('my_hash')
print({key.decode('utf-8'): value.decode('utf-8') for key, value in my_hash.items()})
