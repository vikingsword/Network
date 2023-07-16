import concurrent.futures
import time
import requests
from bs4 import BeautifulSoup

'''
    wallhaven wallpaper download
    for sketchy sort by favorites in last years 
    if cannot download files please check cookie useful or not
'''


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Referer': 'https://wallhaven.cc',
    'Cookie': 'wallhaven_session=eyJpdiI6InFUOHF4UjdWVzQ3YzVOc3NWNWdGdHc9PSIsInZhbHVlIjoiTGF2a3Y5bmpEbnpIVk0wXC9hQk1JRzV3eEFPc1JzZ0o0SU1xR3JEZEZFeGJWUUxLRDQ1TzJ2M1wvb3lMeitXNHZ3IiwibWFjIjoiZWJhYTFlNzU3NTVlYmU4NWY1N2MyMGUxZjA3ZDUyMGEyNDNlMDhlOGNkZWYxMzFmZjBiZTE3MTA1MWM4NzcyNyJ9'
}

proxies = {
    'http': 'http://{}'.format('127.0.0.1:10808')
}

# general | from 1 to 754 about 88gb
url_general = 'https://wallhaven.cc/search?categories=100&purity=010&sorting=favorites&order=desc&ai_art_filter=1&page='
# anime | from 1 to 3161 about 370gb
url_anime = 'https://wallhaven.cc/search?categories=010&purity=010&sorting=favorites&order=desc&ai_art_filter=1&page='
# people | from 1 to 7181 about 841gb     11059
url_people = 'https://wallhaven.cc/search?categories=001&purity=010&sorting=favorites&order=desc&ai_art_filter=1&page='
# total page 11059 about 1300gb

path_general = r'J:\WallPaper\Sketchy\General\\'
path_anime = r'J:\WallPaper\Sketchy\Anime\\'
path_people = r'J:\WallPaper\Sketchy\People\\'


target = url_people
path = path_people
start_page = 1
end_page = 300
thread_num = 30


def getSoup(target):
    resp = requests.get(url=target, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    return BeautifulSoup(html, 'html.parser')


def getUrls(url):
    # get the url list to download
    urls = []
    # people:  ---- >   800
    # general ---->  200
    # anime ---->  200
    for page in range(start_page, end_page):
        # pages.append(page)
        urls.append(url + str(page))
    return urls


def download_file(url, page):
    soup = getSoup(url)
    text = soup.find_all('img', alt='loading')

    # print('第 ' + str(page) + ' 页 开始下载')

    count = 1
    for item in text:
        src = item['data-src']

        pic_name_original = src.split('/')[5]
        if pic_name_original in os.listdir(path):
            continue
        # print('pic_name_original = ' , pic_name_original)
        pic_name_final = 'wallhaven-' + src.split('/')[5]
        # print('pic_name_final = ', pic_name_final)

        src = str(src).replace('th', 'w').replace('small', 'full').replace(pic_name_original, pic_name_final)

        t1 = float(time.time())
        result = requests.get(src, headers=headers, stream=True)
        if result.status_code == 200:
            # download picture
            open(path + pic_name_original, 'wb').write(result.content)
            t2 = float(time.time())
            t = str(round(t2 - t1, 2))
            print('page = ' + str(page) + ' 第 ' + str(count) + ' 张 完成 | 用时 ' + t)
            count = count + 1


def main():
    urls = getUrls(target)
    # print(urls)

    # create threading pool
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_num) as executor:
        # commit task
        download_tasks = {
            executor.submit(download_file, url, i + start_page): url
            for i, url in enumerate(urls)
        }

        # Wait for completion
        for future in concurrent.futures.as_completed(download_tasks):
            url = download_tasks[future]
            try:
                future.result()
            except Exception as e:
                print('Error occurred while downloading file from {}: {}'.format(url, e))


if __name__ == '__main__':
    main()