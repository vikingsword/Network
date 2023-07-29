import requests
from bs4 import BeautifulSoup

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
# 控制台乱码就加上content
resp = requests.get(url=url, headers=headers).content
soup = BeautifulSoup(resp, 'lxml')
li_list = soup.find('div', class_='book-mulu').find_all('li')
with open('result/sanguo.txt', 'w', encoding='utf-8') as f:
    for item in li_list:
        sub_title = item.find('a').text
        sub_link = 'https://www.shicimingju.com' + item.find('a')['href']

        resp2 = requests.get(url=sub_link, headers=headers).content
        soup2 = BeautifulSoup(resp2, 'lxml')
        detail_content = soup2.find('div', class_='chapter_content').text.strip()

        f.write(sub_title + '\n' + detail_content + '\n')
