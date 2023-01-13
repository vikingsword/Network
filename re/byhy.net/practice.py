import os
import re

import requests
from bs4 import BeautifulSoup

url = 'http://www.listeningexpress.com/studioclassroom/ad/'
req = requests.get(url=url)
soup = BeautifulSoup(req.text, 'html.parser')
list = soup.find('div', id='proglist').find_all('a')
for i in list:
    res = re.findall(r'javascript:p\(\'(sc-ad.*?\.mp3)', i['href'])[0]
    result = str(res).replace('\\', '').replace(' ', '%20')
    target = url + result
    command = 'wget ' + target
    # os.system(command)
    print(command)
