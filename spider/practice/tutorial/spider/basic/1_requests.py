import requests

url = 'https://www.sogou.com/'
resp = requests.get(url=url)
with open('result/sogou.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)

