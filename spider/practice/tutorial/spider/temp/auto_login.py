import time

import ddddocr
import requests
from lxml import etree

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}


def get_recaptcha_code():
    recaptcha_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    resp = requests.get(url=recaptcha_url, headers=headers).content
    tree = etree.HTML(resp)
    img_name = tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_url = 'https://so.gushiwen.cn/' + img_name
    resp2 = requests.get(url=img_url, headers=headers).content
    with open('result/' + img_name, 'wb') as f:
        f.write(resp2)
    time.sleep(0.2)

    # ocr
    ocr = ddddocr.DdddOcr()
    with open('./result/' + img_name, 'rb') as fb:
        img_bytes = fb.read()
    code = ocr.classification(img_bytes)
    return code


def login():
    phone_number = input('input your phone number')
    recaptcha_code = get_recaptcha_code()
    data = {
        '__VIEWSTATE': 'T/l1ddicrp1AcJT3OD/eNY4Gn4K8/SqVLFIelvplzlUCw1F+9cvPinbhf05eG74KNJ4LejNDC/y71xSZtqHZ1/CGnKaO45Vzd5R7sYLZkcxEJmd32zEtzI7fgzEhFiDWvY1EIJfqBqEWCZuzpQ3QRhf9AO0=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': phone_number,
        'pwd': 'qweasd123',
        'code': recaptcha_code,
        'denglu': '登录',
    }
    resp = requests.post(url=url, headers=headers, data=data).content


if __name__ == '__main__':
    login()
