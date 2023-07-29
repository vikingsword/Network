import requests
from lxml import etree

url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
resp = requests.get(url=url, headers=headers).content

tree = etree.HTML(resp)

# 热门城市
hot_cities_li = tree.xpath('//div[@class="hot"]//div[@class="bottom"]/ul/li')
for li in hot_cities_li:
    hot_city = li.xpath('./a/text()')[0]
    print(hot_city)

# 全部城市
all_cities_li = tree.xpath('//div[@class="all"]//div[@class="bottom"]/ul/div[2]/li')
count = 0
for li in all_cities_li:
    city = li.xpath('./a/text()')[0]
    # print(city)
    count += 1
# print(count)