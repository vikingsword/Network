import time
import uuid

import ddddocr
import requests
from lxml import etree

url_register = 'https://www.9vps.com/register.asp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
resp = requests.get(url=url_register, headers=headers).content
tree = etree.HTML(resp)
vcode_path = tree.xpath('//*[@id="vcodeimg"]/@src')[0]
vcode_path = 'https://www.9vps.com/' + vcode_path
print(vcode_path)

# url = 'https://www.9vps.com/userreg/vcode.asp'
# resp2 = requests.get(url=url, headers=headers).content
# file_name = str(uuid.uuid4()) + '.jpg'
# file_path = './captcha/' + file_name
#
#
# with open(file_path, 'wb') as f:
#     f.write(resp2)
#
# time.sleep(0.1)
#
# with open(file_path, 'rb') as fb:
#     img_bytes = fb.read()
# ocr = ddddocr.DdddOcr()
# res = ocr.classification(img_bytes)
# res = str(res)
#
# url2 = 'https://www.9vps.com/userreg/getcode.asp'
#
# data = {
#     'SendNum': '18845728919',
#     'vcode': res
# }
# resp2 = requests.post(url=url2, headers=headers, data=data)
# print(resp2.text)
#
