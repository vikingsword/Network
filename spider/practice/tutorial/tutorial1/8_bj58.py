import requests
from lxml import etree

url = 'https://bj.58.com/ershoufang/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
resp = requests.get(url=url, headers=headers)
# print(resp.text)

tree = etree.HTML(resp.text)
title = tree.xpath('//div[@class="property-content-title"]/h3//text()')
with open('result/58.txt', 'w', encoding='utf-8') as f:
    for item in title:
        # 如果需要局部解析 xpath 需要加 ./
        f.write(str(item) + '\n')

'''
//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]/div[1]/h3
'''
