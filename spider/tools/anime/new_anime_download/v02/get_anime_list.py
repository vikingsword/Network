# !usr/bin/env python
# -*- coding:utf-8 _*-
from lxml import etree


def get_urls():
    url_list = list()
    for url in open('anime_homepage.txt', 'r', encoding='utf-8'):
        url = url.strip()
        url_list.append(url)
    return url_list


def get_episode(driver):
    urls = get_urls()
    episode_list = list()

    for url in urls:
        driver.get(url)
        page_source = driver.page_source
        tree = etree.HTML(page_source)
        li = tree.xpath('//div[@id="main0"]/div[@class="movurl mod"]/ul/li[last()]')[0]
        title = li.xpath('./a/@title')[0]
        href = li.xpath('./a/@href')[0]
        file_name = str(driver.title + '-' + title)
        episode_url = 'https://www.ntdm9.com' + href
        episode_list.append([file_name, episode_url])

    for episode in open('anime_list.txt', 'w', encoding='utf-8'):
        f.write(episode[0] + '|' + episode[1] + '\n')
    print('get episode successfully')


def get_list_len():
    count = 0
    for line in open('anime_list.txt', 'r', encoding='utf-8'):
        count += 1
    return count


if __name__ == '__main__':
    i = get_list_len()
    print(i)