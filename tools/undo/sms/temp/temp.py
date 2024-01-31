import requests
from bs4 import BeautifulSoup

url = 'https://www.9vps.com/userreg/vcode.asp?id=0.37953683781843'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

resp = requests.get(url=url, headers=headers).content

with open('1.jpg', 'wb') as f:
    f.write(resp)

# print(resp)

