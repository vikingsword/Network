import asyncio
import re

import aiohttp
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
base_url = 'https://www.biquge7.xyz'


def get_top_books_info():
    top_book_info = {}
    for page in range(1, 2):
        top_url = 'https://www.biquge7.xyz/ph?page=' + str(page)
        resp = requests.get(url=top_url, headers=headers).content
        tree = etree.HTML(resp)
        book_urls = tree.xpath('//div[@class="tui"]//div[@class="title"]/a/@href')
        book_titles = tree.xpath('//div[@class="tui"]//div[@class="title"]/a/text()')
        pairs = zip(book_titles, book_urls)
        top_book_info.update(dict(pairs))
    return top_book_info


def get_detail_urls(book_url):
    resp = requests.get(url=book_url, headers=headers).content

    tree = etree.HTML(resp)
    a_link = tree.xpath('//div[@class="list"]//a/@href')
    url_list = []
    for item in a_link:
        url_detail = 'https://www.biquge7.xyz' + item
        url_list.append(url_detail)
    return url_list


def get_content(file, url):
    # 具体的下载逻辑
    # 获取每一章节的文本，写入file
    for detail_url in get_detail_urls(url):
        resp = requests.get(url=detail_url, headers=headers).content
        chapter_content = parse_content(resp)
        file.write(chapter_content)


def parse_content(response):
    tree = etree.HTML(response)
    chapter = tree.xpath('//div[@class="list list_text"]/h1/text()')[0]
    content_list = tree.xpath('//div[@class="list list_text"]/div[@class="text"]/text()')
    content = keep_chinese_with_punctuation(''.join(content_list))
    print('正在下载 ' + chapter)
    return str(chapter + '\n' + content + '\n')


def keep_chinese_with_punctuation(text):
    # 使用正则表达式匹配中文字符和中文标点符号，并将非中文字符和非中文标点符号替换为空字符串
    chinese_pattern = re.compile(r'[^\u4e00-\u9fa5\u3000-\u301e\uff01-\uff0f\uff1a-\uff20\uff3b-\uff40\uff5b-\uff65]')
    chinese_text = chinese_pattern.sub('', text)
    return chinese_text


if __name__ == '__main__':

    book_dict = get_top_books_info()
    for key, value in book_dict.items():
        # url 为每本书的详情页
        url = base_url + value
        file_path = 'res/' + key + '.txt'
        file = open(file_path, 'a+', encoding='utf-8')
        print('正在下载 ' + key)
        get_content(file, url)
