from bs4 import BeautifulSoup

# markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
# soup = BeautifulSoup(markup, 'html.parser')
# comment = soup.b.string
# print(comment)
#
# doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
# footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
# doc.find(text="INSERT FOOTER HERE").replace_with(footer)
# print(doc)

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
# print(soup.body.b.text)
print(soup.head)
head_tag = soup.head
print(head_tag.contents)

print(soup.find('a').contents)
name_list = list()
print('----------')
list(map(lambda name: name_list.append(name.text), soup.find_all('a')))
print(name_list)
print('----------')

a_list = soup.find_all('a')
for item in a_list:
    print(item.text)

print(soup.head)
print(soup.head.contents)
print(soup.head.contents[0])
print(soup.head.contents[0].contents)
print(soup.head.contents[0].contents[0])
# A string does not have .contents, because it can’t contain anything:
# print(soup.head.contents[0].contents[0].contents)  nothing

a_link = soup.find('a').contents
print(len(a_link))

h_link = soup.head
print(len(h_link))


title_soup = soup.find('title')
for child in title_soup.children:
    print(child.text)

for child in soup.head:
    print(child)

print('+++++++++++++++')
for child in soup.head.descendants:
    print(child)

print(len(list(soup.head.descendants)))













