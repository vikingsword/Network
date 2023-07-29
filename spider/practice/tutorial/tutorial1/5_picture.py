import requests

url = 'https://img2.baidu.com/it/u=1659552792,3869332496&fm=253&fmt=auto&app=120&f=JPEG?w=1280&h=800'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
# content 返回的是 二进制的数据
resp = requests.get(url=url, headers=headers).content

with open('result/pic.jpg', 'wb') as f:
    f.write(resp)