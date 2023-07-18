from bs4 import BeautifulSoup

# with open('bs4.html', 'r') as f:
#     soup = BeautifulSoup(f, 'html.parser')
#     list(map(lambda link: print(link.get('href')), soup.find_all('a')))
#
# soup2 = BeautifulSoup('<title>hello vikingar!</title>', 'html.parser')
# print(soup2.title.text)
# print(soup2)

# <b class="boldest">Extremely bold</b> 是一个标签
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(tag.name)
print(tag.attrs)

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
print(css_soup.p['class'])
print(css_soup.find('p')['class'])

no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
print(no_list_soup.p['class'])

xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
print(xml_soup.p['class'])