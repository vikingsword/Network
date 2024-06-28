# !usr/bin/env python
# -*- coding:utf-8 _*-
class Demo:

    # def __init__(self, name):
    #     this.name = name

    def get(self):
        print(1)




if __name__ == '__main__':
    demo = Demo
    arr = [1, "23", [213, 2.2], demo]
    for e in arr:
        print(e)
