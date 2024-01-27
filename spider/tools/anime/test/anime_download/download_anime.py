# !usr/bin/env python
# -*- coding:utf-8 _*-
import time
import concurrent.futures
import requests

from get_anime_list import get_episode
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_driver():
    edge_option = webdriver.EdgeOptions()
    edge_option.add_argument('--headless')
    edge_option.add_argument('--gpu-disable')
    driver = webdriver.Edge(options=edge_option)
    driver.implicitly_wait(30)
    return driver


def download_handler(driver, filename, url):
    driver.get(url)

    td_element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//table//td[@id="playleft"]'))
    )

    iframe_element = td_element.find_element(By.TAG_NAME, 'iframe')

    driver.switch_to.frame(iframe_element)
    iframe_page_source = driver.page_source
    tree = etree.HTML(iframe_page_source)
    anime_src = tree.xpath('//video[@id="lelevideo"]/@src')[0]
    print("anime_src = ", anime_src)


def download_anime(driver):
    episode_list = list()
    with open('anime_list.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            file_name = line.split('|')[0]
            url = line.split('|')[1]
            episode_list.append([file_name, url])

    for episode in episode_list:
        file_name = episode[0]
        url = episode[1]
        print('filename = {}, url = {}'.format(file_name, url))
        download_handler(driver, file_name, url)
        time.sleep(2)


if __name__ == '__main__':
    driver = init_driver()

    flag, driver = get_episode(driver=driver)
    if flag:
        download_anime(driver)
    # download_anime(driver)