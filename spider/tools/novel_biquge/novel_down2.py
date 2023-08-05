import asyncio
import re

import aiohttp
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
base_url = 'https://www.biquge7.xyz'


def get_top_books_url():
    top_book_list = []
    for page in range(1, 3):
        top_url = 'https://www.biquge7.xyz/ph?page=' + str(page)
        resp = requests.get(url=top_url, headers=headers).content
        tree = etree.HTML(resp)
        book_urls = tree.xpath('//div[@class="tui"]//div[@class="title"]/a/@href')
        for item in book_urls:
            url = base_url + item
            top_book_list.append(url)
    return top_book_list


def get_detail_urls():
    url_main = 'https://www.biquge7.xyz/50416'

    resp = requests.get(url=url_main, headers=headers).content

    tree = etree.HTML(resp)
    a_link = tree.xpath('//div[@class="list"]//a/@href')
    url_list = []
    for item in a_link:
        url_detail = 'https://www.biquge7.xyz' + item
        url_list.append(url_detail)
    return url_list


async def get_content(url):
    # 具体的下载逻辑- 异步协程
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url, headers=headers) as resp:
            res = await resp.text()
            try:
                content, file_name = parse_content(res)
                save_to_file('res/' + file_name, content)
            except Exception as e:
                pass


def parse_content(response):
    tree = etree.HTML(response)
    title = tree.xpath('//div[@class="list list_text"]/h1/text()')[0]
    content_list = tree.xpath('//div[@class="list list_text"]/div[@class="text"]/text()')
    content = keep_chinese_with_punctuation(''.join(content_list))
    print('正在下载 ' + title)
    file_name = str(re.findall(r'/(\d+)$', url)[0]) + '.txt'
    return str(title + '\n' + content + '\n'), file_name


def save_to_file(file_path, content):
    with open(file_path, 'a+', encoding='utf-8') as file:
        file.write(content)


def keep_chinese_with_punctuation(text):
    # 使用正则表达式匹配中文字符和中文标点符号，并将非中文字符和非中文标点符号替换为空字符串
    chinese_pattern = re.compile(r'[^\u4e00-\u9fa5\u3000-\u301e\uff01-\uff0f\uff1a-\uff20\uff3b-\uff40\uff5b-\uff65]')
    chinese_text = chinese_pattern.sub('', text)
    return chinese_text


if __name__ == '__main__':
    # urls = [
    #     'https://www.biquge7.xyz/50416/1',
    #     'https://www.biquge7.xyz/50416/2',
    #     'https://www.biquge7.xyz/50416/3'
    # ]

    urls = get_detail_urls()

    tasks = []
    for url in urls:
        c = get_content(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))


