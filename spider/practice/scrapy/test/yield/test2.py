# !usr/bin/env python
# -*- coding:utf-8 _*-

def mygenerater(n):
    for i in range(n):
        print('开始生成...')
        yield i
        print('完成一次...')


if __name__ == '__main__':
    g = mygenerater(2)
    # 获取生成器中下一个值
    result = next(g)
    print(result)
    result = next(g)
    print(result)
