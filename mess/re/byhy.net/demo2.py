import re

print('1-----------------')
con1 = '''
苹果.是绿色的
橙子.是橙色的
香蕉.是黄色的
'''
partition = re.compile(r'.*\.')
for one in partition.findall(con1):
    print(one)

print('2-----------------')
content = 'a1b2c3d4e5'
for one in re.findall(r'\d', content):
    print(one, end="\t")
print()
for one in re.findall(r'[^a-z]', content):
    print(one, end='\t')
print()
for one in re.findall(r'\D', content):
    print(one, end='\t')
print()
for one in re.findall(r'[^\d]', content):
    print(one, end='\t')
print()

print('3-----------------')
content = '''
001-苹果价格-60
002-橙子价格-70
003-香蕉价格-80'''
partition = re.compile(r'^.*?-', re.M)
for one in partition.findall(content):
    print(one)
partition2 = re.compile(r'^\d+', re.M)
for one in partition2.findall(content):
    print(one)

print('4-----------------')
content = '''
001-苹果价格-60
002-橙子价格-70
003-香蕉价格-80'''
partition = re.compile(r'\d+$', re.M)
for one in partition.findall(content):
    print(one)

print('5-----------------')
content = '''
001-苹果价格-60
002-橙子价格-70
003-香蕉价格-80'''
partition = re.compile(r'[苹果|橙]')
for i in partition.findall(content):
    print(i, end='\t')
