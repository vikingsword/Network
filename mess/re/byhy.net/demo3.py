import re

from bs4 import BeautifulSoup

print('1--------------')
content = '''
苹果，苹果是绿色的
橙子，橙子是橙色的
香蕉，香蕉是黄色的
'''
partition = re.compile(r'^(.*)，', re.M)
for i in partition.findall(content):
    print(i)

print('2--------------')
content = '''
张三，手机号码15945678901
李四，手机号码13945677701
王二，手机号码13845666901
'''
partition = re.compile(r'(.*)，手机号码(\d{11})', re.M)
for i in partition.findall(content):
    print(i)
print()
p = re.compile(r'^(.+)，.+(\d{11})', re.MULTILINE)
for one in p.findall(content):
    print(one)
print()
partition = re.compile(r'(?P<name>.+)，.+(?P<phone>\d{11})', re.M)
for i in partition.finditer(content):
    print(i.group('name'))
    print(i.group('phone'))

print('3----------------')
content = '''
<div class="el">
        <p class="t1">           
            <span>
                <a>Python开发工程师</a>
            </span>
        </p>
        <span class="t2">南京</span>
        <span class="t3">1.5-2万/月</span>
</div>
<div class="el">
        <p class="t1">
            <span>
                <a>java开发工程师</a>
            </span>
		</p>
        <span class="t2">苏州</span>
        <span class="t3">1.5-2/月</span>
</div>
'''
soup = BeautifulSoup(content, 'html.parser')
html = soup.findAll('p', attrs={'class', 't1'})  # html's type is byte
print(html)
print()
partition = re.compile(r'<a>(.*)</a>', re.M)
for i in partition.findall(content):
    print(i)
print()
p = re.compile(r'class=\"t1\">.*?<a>(.*?)</a>', re.DOTALL)
for one in p.findall(content):
    print(one)
