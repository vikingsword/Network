import re

print('1.-----------')
# print(re.sub(r'^[a-c]+', '', 'abc123'))

print('2.---------------')
# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")

print('3.---------------')
phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
# num = re.sub(r'#.*$', "", phone)
num1 = re.sub(r'#.*$', '', phone)
print("电话号码是: ", num1)

# delete string that not number like '-'
num = re.sub(r'\D', '', phone)
print("电话号码是 : ", num)


# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))


pattern = re.compile(r'\d+')
m = pattern.match('sdfjslo123dfsldfj')
print(m)










