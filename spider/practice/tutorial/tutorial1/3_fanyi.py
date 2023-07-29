import json

import requests

url = 'https://fanyi.baidu.com/sug'
key = input('input your key: ')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
param = {
    'kw': key
}
resp = requests.post(url=url, data=param, headers=headers)

resp.encoding = 'utf-8'
# res 为 json 对象
res = resp.json()

# 持久化
fileName = key + '.json'
fp = open('result/' + fileName, 'w', encoding='utf-8')
json.dump(res, fp, ensure_ascii=False)

print(key + ' 翻译完成！ ')