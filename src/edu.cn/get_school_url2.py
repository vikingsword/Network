import queue
import threading

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

proxies = {
    'http': 'http://127.0.0.1:10808'
}


def getSchoolUrls():
    while not q.empty():
        school_url = ''
        school_name_url = q.get()
        school_name2 = str(school_name_url).split('|')[0]
        search_url = str(school_name_url).split('|')[1]
        try:
            resp = requests.get(url=search_url, headers=headers, proxies=proxies)
            soup = BeautifulSoup(resp.text, 'html.parser')
            school_url = soup.find('cite', class_='apx8Vc tjvcx GvPZzd cHaqb').contents[0]
        except Exception as e:
            pass

        with open('school_urls2.txt', 'a+', encoding='utf-8') as f:
            f.write(school_name2 + ':' + school_url + '\n')
    f.close()


if __name__ == '__main__':
    q = queue.Queue()
    for school_name in open('school_name.txt', 'r', encoding='utf-8'):
        school_name = school_name.strip() + '官网'
        url = 'https://www.google.com/search?q=' + str(school_name)
        # 使用 冒号 q.get() 无法获取到第二个值
        q.put(school_name + '|' + url)

    for item in range(10):
        t = threading.Thread(target=getSchoolUrls)
        t.start()
