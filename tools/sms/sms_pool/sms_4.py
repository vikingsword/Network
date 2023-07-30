import time
import uuid

import ddddocr
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
url = 'https://www.9vps.com/userreg/vcode.asp?id=0.3704409555678817'
resp2 = requests.get(url=url, headers=headers).content
file_name = str(uuid.uuid4()) + '.jpg'
file_path = './captcha/' + file_name


with open(file_path, 'wb') as f:
    f.write(resp2)

time.sleep(0.1)

with open(file_path, 'rb') as fb:
    img_bytes = fb.read()
ocr = ddddocr.DdddOcr()
res = ocr.classification(img_bytes)
res = str(res)

url2 = 'https://www.9vps.com/userreg/getcode.asp'

data = {
    'SendNum': '18845728919',
    'vcode': res
}
resp2 = requests.post(url=url2, headers=headers, data=data)
print(resp2.text)

