import uuid
import ddddocr
import requests

url = 'https://so.gushiwen.cn/RandCode.ashx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
resp = requests.get(url=url, headers=headers).content
file_name = str(uuid.uuid4()) + '.ashx'
print(file_name)

with open('result/' + file_name, 'wb') as f:
    f.write(resp)
ocr = ddddocr.DdddOcr()
with open('result/' + file_name, 'rb') as fp:
    img_bytes = fp.read()
img_res = ocr.classification(img_bytes)
print(img_res)
