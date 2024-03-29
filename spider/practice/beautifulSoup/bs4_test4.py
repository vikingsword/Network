from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# for item in soup.find_all('a'):
#     print(item.string)
#     print(item.get('href'))

demo = soup.find_all('a', attrs={'class', 'sister'})
list(map(lambda x: print(x.string), demo))
# for item in demo:
#     print(item.text)

for string in soup.strings:
    print(repr(string))

print('===========')

for string in soup.stripped_strings:
    print(repr(string))

print('--------------')

for parent in soup.find('a').parents:
    print(parent.name)

print('--------------')

print(soup.html.parent.name)

print(soup.find_all('b'))

print(soup.find_all('b')[0])

for item in soup.find_all(re.compile('^b')):
    print(item)

print('------------')
for item in soup.find_all(re.compile('^title')):
    print(item)

print('=======')

a_b_tag = soup.find_all(['a', 'b'])
for item in a_b_tag:
    print(item)

print('-------------')


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


tag1 = soup.find_all(has_class_but_no_id)
print(tag1)
