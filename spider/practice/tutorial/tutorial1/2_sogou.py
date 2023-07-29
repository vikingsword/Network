import requests

key = input('input your key: ')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
param = {
    'query': key
}
url = 'https://sogou.com/web'
resp = requests.get(url=url, params=param, headers=headers)
res = resp.text
fileName = key + '.html'
with open('result/' + fileName, 'w', encoding='utf-8') as f:
    f.write(res)
print(fileName + '保存成功')
