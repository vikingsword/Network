# from https://www.byhy.net/tut/py/extra/regex/
import re

print('1-----------')
content1 = '''
Python3 高级开发工程师 上海互教教育科技有限公司上海-浦东新区2万/月02-18满员
测试开发工程师（C++/python） 上海墨鹍数码科技有限公司上海-浦东新区2.5万/每月02-18未满员
Python3 开发工程师 上海德拓信息技术股份有限公司上海-徐汇区1.3万/每月02-18剩余11人
测试开发工程师（Python） 赫里普（上海）信息科技有限公司上海-浦东新区1.1万/每月02-18剩余5人
Python高级开发工程师 上海行动教育科技股份有限公司上海-闵行区2.8万/月02-18剩余255人
python开发工程师 上海优似腾软件开发有限公司上海-浦东新区2.5万/每月02-18满员
'''

for one in re.findall(r'([\d.]+)万/每{0,1}月', content1):
    print(one)

print('2-----------')
content2 = '''苹果是绿色的
橙子是橙色的
香蕉是黄色的
乌鸦是黑色的'''

for one in re.findall(r'.色', content2):
    print(one)

print('3-----------')
content3 = '''
苹果，是绿色的
橙子，是橙色的
香蕉，是黄色的
乌鸦，是黑色的
猴子，
'''
for one in re.findall(r'，.*', content3):
    print(one)

for one in re.findall(r'，.+', content3):
    print(one)

for one in re.findall(r'，.?', content3):
    print(one)

print('4-----------')
content4 = '红彤彤，绿油油，黑乎乎，绿油油油油'
for one in re.findall(r'.油{2}', content4):
    print(one)
print()
for one in re.findall(r'.油{2,4}', content4):
    print(one)

print('5------------')
source = '<html><head><title>Title</title>'
for one in re.findall(r'<.*>', source):
    print(one)
print()
for one in re.findall(r'<.*?>', source):
    print(one)