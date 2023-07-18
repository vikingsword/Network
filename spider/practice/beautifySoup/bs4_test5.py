import re

from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
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
# find_all return a list
print(soup.find_all('p', 'title'))

print(soup.find_all('a'))

print(soup.find_all(id='link2'))
print(soup.find_all(id='link2')[0].text)

print(soup.find_all(string=re.compile('sister')))

print(soup.find_all('a', href=re.compile('tillie')))

print(soup.find_all(href=re.compile('tillie'), id='link3', attrs={'class': 'sister'}))
print('-------')
print(soup.find_all(attrs={'class': 'sister', 'id': 'link3'}))

# name, class and data-foo param can't use for param in find_all but can in attrs
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'html.parser')
# print(data_soup.find_all(data-foo='value'))
print(data_soup.find_all('div', attrs={'data-foo': 'value'}))

# use class_ instead of class
print(soup.find_all('a', class_='sister'))


def has_six_char(css_class):
    return css_class is not None and len(css_class) == 6


def href_filter(href_info):
    return href_info is not None and 'ti' in href_info


print(soup.find_all(class_=has_six_char, href=href_filter))

print('-------------')

print(soup.find_all('a', limit=1))
