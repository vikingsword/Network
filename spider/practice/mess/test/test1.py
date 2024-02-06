# !usr/bin/env python
# -*- coding:utf-8 _*-


class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.app = str(name) + '-' + str(age)



if __name__ == '__main__':
    test = Test('zs', 19)
    print(test.name)
    print(test.age)
    print(test.app)