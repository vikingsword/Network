# !usr/bin/env python
# -*- coding:utf-8 _*-

# 在方法中使用self主要是为了让方法能够访问类实例中的属性和方法

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get(self):
        print('name = ', self.name)


if __name__ == '__main__':
    person = Person('vikingar', 1)
    person.get()
