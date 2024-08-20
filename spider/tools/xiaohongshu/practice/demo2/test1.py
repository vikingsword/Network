# !usr/bin/env python
# -*- coding:utf-8 _*-
import requests
from lxml import etree


def read_cookie():
    with open('cookie.txt', 'r') as f:
        return f.read()


url = 'https://www.xiaohongshu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'cookie': str(read_cookie())
}
res = requests.get(url=url, headers=headers)
tree = etree.HTML(res.text)
section_list = tree.xpath('//*[@id="exploreFeeds"]')

for item in section_list:
    print("title = ", item.text)

