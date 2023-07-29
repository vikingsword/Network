import json

import requests

url = 'https://movie.douban.com/j/chart/top_list'
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20',
}
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

resp = requests.get(url=url, params=param, headers=headers)
res = resp.json()

fp = open('result/douban.json', 'w', encoding='utf-8')
json.dump(res, fp, ensure_ascii=False)

print('获取完成！ ')
