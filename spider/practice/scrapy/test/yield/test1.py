# !usr/bin/env python
# -*- coding:utf-8 _*-

def generator():
    for i in range(1, 10):
        yield i * i


gen = generator()
print('gen = ', gen)
print('next(gen): ', next(gen))
print('next(gen): ', next(gen))



