import requests
from bs4 import BeautifulSoup


def getSoup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


url = "https://wallhaven.cc/search?categories=111&purity=010&topRange=1y&sorting=toplist&order=desc&ai_art_filter=0&page="
for page in range(1, 2):
    target = url + str(page)
    # print(target)
    soup = getSoup(target)
    text = soup.find_all('img', alt='loading')
    print(page)
    with open('src.txt', 'a+') as f:
        for item in text:
            src = item['data-src']

            picName1 = src.split('/')[5]
            picName2 = 'wallhaven-' + src.split('/')[5]
            # src.replace(picName1, picName2)
            src = str(src).replace('th', 'w').replace('small', 'full').replace(picName1, picName2)
            print(src)
            f.write(src + "\n")
f.close()

# https: // th.wallhaven.cc / small / kx / kxwkd6.jpg
# https://w.wallhaven.cc/full/kx/wallhaven-kxwkd6.jpg
