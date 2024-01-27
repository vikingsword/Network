# !usr/bin/env python
# -*- coding:utf-8 _*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree


def get_urls():
    url_list = list()
    with open('anime_homepage.txt', 'r', encoding='utf-8') as f:
        for url in f:
            url = url.strip()
            url_list.append(url)
    return url_list


def get_episode(driver):
    urls = get_urls()
    episode_list = list()
    file_name = None

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

    if urls.__len__() != episode_list.__len__():
        print('get episode error, try again ')
        return False, driver
    else:
        with open('anime_list.txt', 'w', encoding='utf-8') as f:
            for episode in episode_list:
                f.write(episode[0] + '|' + episode[1] + '\n')
        print('get episode successfully')
        return True, driver
