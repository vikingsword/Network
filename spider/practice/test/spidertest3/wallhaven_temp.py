import concurrent.futures
import time
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Referer': 'https://wallhaven.cc',
    'Cookie': 'wallhaven_session=eyJpdiI6InFUOHF4UjdWVzQ3YzVOc3NWNWdGdHc9PSIsInZhbHVlIjoiTGF2a3Y5bmpEbnpIVk0wXC9hQk1JRzV3eEFPc1JzZ0o0SU1xR3JEZEZFeGJWUUxLRDQ1TzJ2M1wvb3lMeitXNHZ3IiwibWFjIjoiZWJhYTFlNzU3NTVlYmU4NWY1N2MyMGUxZjA3ZDUyMGEyNDNlMDhlOGNkZWYxMzFmZjBiZTE3MTA1MWM4NzcyNyJ9'
}

proxies = {
    'http': 'http://{}'.format('127.0.0.1:10808')
}

# general | from 1 to 446 about 52gb
url1 = 'https://wallhaven.cc/search?categories=100&purity=001&sorting=views&order=desc&ai_art_filter=1&page='
# anime | from 1 to 1299 about 151gb
url2 = 'https://wallhaven.cc/search?categories=100&purity=001&sorting=views&order=desc&ai_art_filter=1&page='
# people | from 1 to 8700 about 1041gb
url3 = 'https://wallhaven.cc/search?categories=100&purity=001&sorting=views&order=desc&ai_art_filter=1&page='
# total 40443 page about 4739gb


path1 = r'J:\WallPaper\nsfw\General\ '
path2 = r'J:\WallPaper\nsfw\Anime\ '
path3 = r'J:\WallPaper\nsfw\People\ '


def getSoup(target):
    resp = requests.get(url=target, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    return BeautifulSoup(html, 'html.parser')


def getUrls(url):
    urls = []
    # pages = []
    for page in range(1, 5):
        # pages.append(page)
        urls.append(url + str(page))
    return urls


def download_file(url, page):
    # for page in range(1, 2):
    path1 = r'J:\WallPaper\nsfw\General\ '
    # print(url)
    soup = getSoup(url)
    text = soup.find_all('img', alt='loading')
    # print(text)

    print('第 ' + str(page) + ' 页 开始下载')

    count = 1
    for item in text:
        src = item['data-src']
        print(src)

        picNameOriginal = src.split('/')[5]
        picNameFinal = 'wallhaven-' + src.split('/')[5]
        # src.replace(picName1, picName2)
        src = str(src).replace('th', 'w').replace('small', 'full').replace(picNameOriginal, picNameFinal)
        print(src)
        t1 = float(time.time())
        result = requests.get(src, headers=headers, stream=True)
        if result.status_code == 200:
            # 下载图片

            open(path1 + picNameOriginal, 'wb').write(result.content)
            t2 = float(time.time())
            t = str(round(t2 - t1, 2))
            print('page = ' + str(page) + ' 第 ' + str(count) + ' 张 完成 | 用时 ' + t)
            count = count + 1


def main():
    urls = getUrls(url1)
    # print(urls)

    # 创建线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # 提交下载任务给线程池
        download_tasks = {
            executor.submit(download_file, url, i + 1): url
            for i, url in enumerate(urls)
        }

        # 等待所有下载任务完成
        for future in concurrent.futures.as_completed(download_tasks):
            url = download_tasks[future]
            try:
                future.result()
            except Exception as e:
                print('Error occurred while downloading file from {}: {}'.format(url, e))


if __name__ == '__main__':
    main()
