'''

fofa 批量请求脚本
url = 'https://fofa.info/result?qbase64=ImdsYXNzZmlzaCIgJiYgcG9ydD0iNDg0OCI%3D&page=1&page_size=10'
url = 'https://fofa.info/result?qbase64=ImdsYXNzZmlzaCIgJiYgcG9ydD0iNDg0OCI=  &page=1&page_size=10

'''
import base64
from bs4 import BeautifulSoup

import requests


def getSoup(target):
    resp = requests.get(url=target)
    resp.encoding = 'utf-8'
    html = resp.text
    return BeautifulSoup(html, 'html.parser')


def getUrl(search_content, page_num, page_size):
    fofa_url = 'https://fofa.info/result?qbase64='

    search_content_encode = base64.b64encode(search_content.encode('utf-8')).decode('utf-8')
    url = fofa_url + search_content_encode + '&page=' + str(page_num) + '&page_size=' + str(page_size)
    return url


if __name__ == '__main__':
    search_content = '"glassfish" && port="4848"'
    page_num = 1
    page_size = 10

    url = getUrl(search_content, page_num, page_size)
    soup = getSoup(url)
    ips = soup.find_all('a', target='_blank')

    for item in ips:
        print(item['href'])


# res = requests.get(url=url).content
# with open('fofa.txt', 'w', encoding='utf-8') as f:
#     f.write(res.decode('utf-8'))
