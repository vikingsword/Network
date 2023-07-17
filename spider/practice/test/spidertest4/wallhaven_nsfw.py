import concurrent.futures
import os
import time
import requests
from bs4 import BeautifulSoup

'''
    wallhaven wallpaper download with multipart threading
    for nsfw sort by favorites in last years 
    if cannot download file please check cookie useful or not
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Referer': 'https://wallhaven.cc',
    'Cookie': 'wallhaven_session=eyJpdiI6IkJsVFZMbDlmM2xsSUNmVTdmN09EK3c9PSIsInZhbHVlIjoiNHZxRW0zYlk0ZUxTdnVZSTR2NUp1eWV0YnFLNDZkUEVrNzNkb3lKNElHSUxHUjJcL0k2SE1MNFpya3ZvMXI2U2kiLCJtYWMiOiJlMTA3N2E3MmQ5YTNlNDY4MzM0MmFhNGM5NmQ5NTUxYmE3OTkyZWJjYTk5NjBkYWJkYjcwNWM2MmEyY2YwY2I2In0%3D'
}

proxies = {
    'http': 'http://{}'.format('127.0.0.1:10808')
}

# general | from 1 to 446 about 52gb
url_general = 'https://wallhaven.cc/search?categories=100&purity=001&sorting=favorites&order=desc&ai_art_filter=1&page='
# anime | from 1 to 1299 about 151gb
url_anime = 'https://wallhaven.cc/search?categories=010&purity=001&sorting=favorites&order=desc&ai_art_filter=1&page='
# people | from 1 to 8700 about 1041gb
url_people = 'https://wallhaven.cc/search?categories=001&purity=001&sorting=favorites&order=desc&ai_art_filter=1&page='


path_general = r'J:\WallPaper\NSFW\General\\'
path_anime = r'J:\WallPaper\NSFW\Anime\\'
path_people = r'J:\WallPaper\NSFW\People2\\'

path_temp = r'J:\WallPaper\NSFW\temp\\'


target = url_people
path = path_people
start_page = 1
end_page = 300
thread_num = 30


# folder_path2 = r'J:\WallPaper\NSFW\People2\\'


def getSoup(target):
    resp = requests.get(url=target, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    return BeautifulSoup(html, 'html.parser')


def getUrls(url):
    # get the url list to download
    urls = []
    # page already download
    # people:  ---- >   800
    # general ---->  200
    # anime ---->  300
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
