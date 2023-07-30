import os.path
import time
import uuid

import ddddocr
import requests
from lxml import etree

url = 'https://www.o571.com/member/register.asp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
# url_send = 'https://www.o571.com/config/api/sms/smssend.asp?piccode=2193&smsclass=1&mobile=18845728919&temp=4483842'
url_send = 'https://www.o571.com/config/api/sms/smssend.asp'


def get_captcha_url():
    resp = requests.get(url=url, headers=headers).content
    tree = etree.HTML(resp)
    code_path = tree.xpath('//form[@id="reg"]//img[@id="pccode"]/@src')[0]
    return 'https://www.o571.com' + code_path


def get_captcha_code():
    code_url = get_captcha_url()
    if not os.path.exists('../sms_pool/captcha'):
        os.mkdir('../sms_pool/captcha')
    resp = requests.get(url=code_url, headers=headers).content
    code_name = str(uuid.uuid4()) + '.jpg'
    code_path = './captcha/' + code_name

    with open(code_path, 'wb') as f:
        f.write(resp)
    time.sleep(0.2)

    with open(code_path, 'rb') as fb:
        img_bytes = fb.read()

    if os.path.exists(code_path):
        os.remove(code_path)

    ocr = ddddocr.DdddOcr()
    res = ocr.classification(img_bytes)
    return res


def send_sms():
    phone_num = input('input your phone number: ')
    params = {
        'piccode': get_captcha_code(),
        'smsclass': 1,
        'mobile': phone_num,
        'temp': 4483842
    }
    resp = requests.get(url=url_send, params=params)
    if resp.status_code == 200:
        print('发送成功！ ')


if __name__ == '__main__':
    send_sms()
