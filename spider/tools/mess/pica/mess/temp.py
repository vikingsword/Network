import requests
from lxml import etree

url = 'http://manhuabika.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
resp = requests.get(url=url, headers=headers)
res = resp.content
print(resp.text)


tree = etree.HTML(resp.content)
li_list = tree.xpath('//div[@id="splide02-list"]/li')
for li in li_list:
    data_src = li.xpath('.//div[@class="card-body"]/img/@data-src')
    title = li.xpath('.//div[@class="card-body"]/h2/@text')
    print(data_src)
    print(title)