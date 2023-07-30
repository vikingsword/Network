import time

import ddddocr
import requests
from lxml import etree

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
resp = requests.get(url=url, headers=headers).content
tree = etree.HTML(resp)
img_name = tree.xpath('//*[@id="imgCode"]/@src')[0]
img_url = 'https://so.gushiwen.cn/' + img_name
resp2 = requests.get(url=img_url, headers=headers).content
with open('result/' + img_name, 'wb') as f:
    f.write(resp2)
time.sleep(0.2)

# ocr
ocr = ddddocr.DdddOcr()
with open('./result/' + img_name, 'rb') as fb:
    img_bytes = fb.read()
res = ocr.classification(img_bytes)
print(res)
