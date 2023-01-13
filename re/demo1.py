import re

url = 'test123'

# get the position of header character
# if exist return pos span, else return none
print('1.------------')
print(re.match(r'test', url).span())
print(re.match(r"123", url))

# get the position of url,
print('2.------------')
print(re.search(r"t1", url))

print('3.------------')
print(re.search(r'^test', url))
print(re.search(r'^test', url).span())

# match none or multi times before 'est'
print('4.------------')
print(re.search(r'est*', 'estest'))
print(re.search(r'ab*', 'a'))  # take a point
print(re.search(r'ab*', 'abbbbb'))

print('5.-------------')
print(re.search(r'12.$', url))

# . match one character
print('6.-------------')
foo = 'foo1\nfoo2\n'
print(re.search(r'foo.$', foo))

# match one or multi times of test
print('7.------------')
print(re.search(r'test+', url))

# match one or multi times before 'ab'
print('8.------------')
print(re.search(r'ab?', 'baa'))

# match m times of character
print('9.------------')
print(re.search(r'test{2}', 'testtest'))
print(re.search(r'a{4}', 'baaaa'))
print(re.search('r{3}', 'bcaaaa'))

# match 3 or 4 or 5 times of 'a'
print('10.-------------')
print(re.search(r'a{3,5}', 'bcaaa'))
print(re.search(r'a{3,5}', 'bcaaaa'))
print(re.search(r'a{3,5}', 'bcaaaa'))
print(re.search(r'ab{3,}', 'abbbbbb'))
