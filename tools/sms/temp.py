import requests
from bs4 import BeautifulSoup

url = 'https://m.139w.com/register.asp'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Cookie': 'PostToken=BjKGnBMD7wBkqE5qRyYnh9StG0HRpl3; ASPSESSIONIDAUCDRRCT=CKFLAMNADPMGFNPDEHPCENCC; ASPSESSIONTDAZBYCXDW=BCD6D9E34A8E2EC4F6300097'
}

resp = requests.get(url=url, headers=headers)

soup = BeautifulSoup(resp.text, 'html.parser')

src = soup.find('div', class_='yhdl_input2').find('img')

print(src)

