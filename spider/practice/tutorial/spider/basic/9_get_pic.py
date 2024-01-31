import os
import time

import requests
from lxml import etree

url = 'https://pic.netbian.com/4kdongman/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
# 如果乱码可以 .content 转化为二进制
resp = requests.get(url=url, headers=headers).text

tree = etree.HTML(resp)
li_list = tree.xpath('//div[@class="slist"]/ul/li')
if not os.path.exists('./result/pic'):
    os.mkdir('./result/pic')
for li in li_list:
    img_link = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
    img_name = li.xpath('./a/b//text()')[0]
    # 如果上面写的是 requests.get(xxx).text 可以针对特定乱码的地方进行如下编码
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    print(img_name)
    try:
        with open('result/pic/' + str(img_name) + '.jpg', 'wb') as f:
            res = requests.get(url=img_link, headers=headers).content
            f.write(res)
            time.sleep(0.2)
    except Exception as e:
        pass

# srcs = tree.xpath('//div[@class="slist"]//li/a/img/@src')
# file_name = tree.xpath('//div[@class="slist"]//li/a/b/text()')
# for item in srcs:
#     img_url = 'https://pic.netbian.com' + item
#     img = requests.get(url=img_url).content
#     with open('result/' + file_name, 'wb', encoding='utf-8') as f:
#         f.write(img)
