'''
— cookie值的来源是哪里？
— 模拟登录post请求后，由服务器端创建。
session会话对象：
    - 作用：
        1．可以进行请求的发送。
        2．如果请求过程中产生了cookie，则该cookie会被自动存储／携带在该session对象
    - 创建一个session对象：requests.Session（）
    - 使用session对象进行模拟登录post请求的发送（cookie就会被存储在session中）
    — session对象对个人主页对应的get请求进行发送（携带了cookie）
    todo wallhaven cookies from session doesn't work
'''

import requests
from lxml import etree

url = 'http://wallhaven.cc/user/Vikingsword'
proxies = {
    'http': 'http://{}'.format('127.0.0.1:10809')
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
session = requests.Session()
resp = session.get(url=url, headers=headers, proxies=proxies)
# print(session.cookies)

with open('result/1.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)

url2 = 'http://wallhaven.cc/search?categories=001&purity=100&topRange=1d&sorting=toplist&order=desc&ai_art_filter=1'

resp2 = session.get(url=url2, headers=headers, proxies=proxies).content
# with open('result/3.html', 'wb') as f:
#     f.write(resp2)
tree = etree.HTML(resp2)
li_list = tree.xpath('//div[@id="thumbs"]/section/ul/li')
for li in li_list:
    src = li.xpath('.//img[@class="lazyload"]/@data-src')[0]
    print(src)
# print(session.cookies)
