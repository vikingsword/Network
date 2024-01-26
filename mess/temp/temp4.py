"""
    扩展列表的sort方法
    在学习了将函数作为参数传递后，我们可以将学习的sort方法对列表进行自定义排序

"""
# 准备列表、
my_list = [["a", 55], ["b", 4], ["c", 11]]


def choose_sort_key(element):
    return element[1]


print(choose_sort_key(my_list))
