import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url = "https://wallhaven.cc/search?categories=111&purity=010&topRange=1y&sorting=toplist&order=desc&ai_art_filter=0&page="
for page in range(16, 17):
    target = url
    # print(target)
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find_all('img', alt='loading')
    print(page)
    with open('src.txt', 'a+') as f:
        for item in text:
            src = item['data-src']
            # todo / kxwkd6.jpg -->  /wallhaven-kxwkd6.jpg
            src = str(src).replace('th', 'w').replace('small', 'full')
            print(src)
            f.write(src + "\n")


# https: // th.wallhaven.cc / small / kx / kxwkd6.jpg
# https://w.wallhaven.cc/full/kx/wallhaven-kxwkd6.jpg
