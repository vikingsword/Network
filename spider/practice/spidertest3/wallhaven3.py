import requests
from bs4 import BeautifulSoup

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
headers2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    'token': "wallhaven_session=eyJpdiI6Im1wUDhIbFZZS1p2VW5qMUFrZEV1TWc9PSIsInZhbHVlIjoiUzlQZ1doblFJbWYrWFBPMGZTUDJyZHRuOUlkZm9IeExtNko1U0dcL3JcL3FVOHZnVzhLSERmMmpONFVQTTdyOTBMIiwibWFjIjoiYTJhNWQyOGVjMWM0YWVjZWI5MmI3M2E5MzYxZDI0OTY5ZTBjNjBjZjFjOWNlODQ1ODBhMjk2Zjg2Nzc0NzZkNiJ9; expires=Sun, 14-May-2023 08:34:35 GMT; Max-Age=7200; path=/; secure; httponly; samesite=strict"
}

proxies = {
    'http': 'http://{}'.format('127.0.0.1:10808')
}

url = 'https://wallhaven.cc/search?categories=011&purity=011&topRange=1y&sorting=toplist&order=desc&ai_art_filter=0&page='

path = r'F:\Wallpaper\wallheaven\nsfw\img2\ '


def getSoup(url):
    resp = requests.get(url=url, headers=headers1)
    resp.encoding = 'utf-8'
    html = resp.text
    return BeautifulSoup(html, 'html.parser')

# 下到第九页
for page in range(25, 50):
    target = url + str(page)
    # print(target)
    soup = getSoup(target)
    text = soup.find_all('img', alt='loading')
    # print(text)
    print("page = " + str(page))

    for item in text:
        src = item['data-src']

        picNameOriginal = src.split('/')[5]
        picNameFinal = 'wallhaven-' + src.split('/')[5]
        # src.replace(picName1, picName2)
        src = str(src).replace('th', 'w').replace('small', 'full').replace(picNameOriginal, picNameFinal)
        # print(src)
        result = requests.get(src, headers=headers1, stream=True)
        if result.status_code == 200:
            # 下载图片
            open(path + picNameOriginal, 'wb').write(result.content)
            print("page = " + str(page) + " done")

# f.close()

# https: // th.wallhaven.cc / small / kx / kxwkd6.jpg
# https://w.wallhaven.cc/full/kx/wallhaven-kxwkd6.jpg
