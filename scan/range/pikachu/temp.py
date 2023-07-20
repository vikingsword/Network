import time

import requests
from bs4 import BeautifulSoup

url = 'http://192.168.110.34/pikachu/vul/burteforce/bf_form.php'

data = {
    'username': 'admin',
    'password': '123456'
}
res = requests.post(url=url, data=data)
with open('file.html', 'a+', encoding='utf-8') as f:
    f.write(res.text)
# if 'success' in res:
#     print('ok')
