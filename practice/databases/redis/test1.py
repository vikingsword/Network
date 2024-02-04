# !usr/bin/env python
# -*- coding:utf-8 _*-
import redis

# 建立线程池，避免重复连接
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)


def my_demo():
    r.set("news1", "http://www.1.com")
    r.set("news2", "http://www.2.com")
    print(r.get("news1"))
    print(r.get("news2"))


if __name__ == '__main__':
    my_demo()

