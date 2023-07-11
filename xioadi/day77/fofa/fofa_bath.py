'''

fofa 批量请求脚本
url = 'https://fofa.info/result?qbase64=ImdsYXNzZmlzaCIgJiYgcG9ydD0iNDg0OCI%3D&page=1&page_size=10'
url = 'https://fofa.info/result?qbase64=ImdsYXNzZmlzaCIgJiYgcG9ydD0iNDg0OCI=  &page=1&page_size=10

'''
import base64
from xml import etree

from bs4 import BeautifulSoup

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Cookie': 'fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6Mjk1Nzg2LCJtaWQiOjEwMDE2NzQzOCwidXNlcm5hbWUiOiJuaWVtYW5kZWEiLCJleHAiOjE2ODkyMjI5ODZ9.b_-dXbr3uhB53x0vjo4iWXZN5L9Tksbnqp8Clok3N-Z_Nu97P-pfNB3ckSLhb1UeBDQW8uThxy8WPx25BUfP_w'
}

headers_temp = {
    'Cookie': '_fofapro_ars_session=01148af6062a060ccd5dd9a8483f5fea'
}


def getSoup(target):
    resp = requests.get(url=target, headers=headers_temp)
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
    # page_num = 1
    page_size = 10

    for page_num in range(1, 11):
        url = getUrl(search_content, page_num, page_size)
        soup = getSoup(url)
        ips = soup.find_all('a', target='_blank')

        for item in ips:
            with open('glassfish_fofa_scan/fofa_ips.txt', 'a+') as f:
                ip = item['href']
                f.write(ip + "\n")
                print(ip)

    # lxml写法
    # soup = etree.HTML(res)
    # ips = soup.xpath('//div[@class="re-domain"]/a[@target="_blank"]/@href')
