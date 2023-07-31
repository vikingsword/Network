import requests
from lxml import etree

url = 'https://www.biquge7.xyz/50416/1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

resp = requests.get(url=url, headers=headers).text
tree = etree.HTML(resp)
title = tree.xpath('//div[@class="list list_text"]/h1/text()')[0]
print(title)
