import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
for line in open('teachers.txt', 'r', encoding='utf-8'):
    line = line.strip()
    name = line.split('|')[0]
    url = line.split('|')[1]

url2 = 'http://ss.sut.edu.cn/info/1176/1839.htm'
resp = requests.get(url=url2, headers=headers).content
tree = etree.HTML(resp)
p_list = tree.xpath('//div[@class="v_news_content"]/p')
for p in p_list:
    content = p.xpath('.//text()')
    with open('test.txt', 'a+', encoding='utf-8') as f:
        f.write(str(content))
