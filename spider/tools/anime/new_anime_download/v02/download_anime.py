# !usr/bin/env python
# -*- coding:utf-8 _*-
import time
import requests
import os
from get_anime_list import get_episode
from get_anime_list import get_list_len
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init_driver():
    edge_option = webdriver.EdgeOptions()
    edge_option.add_argument('--headless')
    edge_option.add_argument('--gpu-disable')
    edge_option.add_argument('--mute-audio')
    driver = webdriver.Edge(options=edge_option)
    driver.implicitly_wait(30)
    return driver


def download_detail(filename, url):
    try:
        # 发送 GET 请求获取视频文件
        response = requests.get(url, stream=True)

        # 检查请求是否成功
        response.raise_for_status()

        # 以二进制写入文件
        path = save_path + filename + ".mp4"
        print('start download: ', filename)
        with open(path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Video downloaded successfully to: {path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading video: {e}")


def download_handler(filename, url):
    time.sleep(1)
    driver2 = init_driver()
    driver2.get(url)
    td_element = WebDriverWait(driver2, 30).until(
        EC.presence_of_element_located((By.XPATH, '//table//td[@id="playleft"]'))
    )
    # print(driver2.page_source)

    iframe_element = td_element.find_element(By.TAG_NAME, 'iframe')
    # todo : 不知道为什么有的时候print一下就可以找到iframe,有的时候不用print就可以
    # print('switch to frame...')

    driver2.switch_to.frame(iframe_element)
    time.sleep(0.5)
    iframe_page_source = driver2.page_source
    tree = etree.HTML(iframe_page_source)
    # print(iframe_page_source)
    anime_src = tree.xpath('//video[@id="lelevideo"]/@src')[0]
    if anime_src is not None:
        with open('anime_src.txt', 'w', encoding='utf-8') as f:
            f.write(filename + '|' + anime_src + '\n')
        download_detail(filename, anime_src)
    else:
        print('anime_src get error')


def save_download(file_name, url):
    retries = 0

    while retries < max_retries:
        try:
            # 尝试执行业务逻辑
            download_handler(file_name, url)
        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            retries += 1
        else:
            # 如果没有发生异常，跳出循环
            break
    else:
        # 如果循环正常结束（未被 break 中断），表示重试次数达到上限
        print("Max retries reached, giving up.")


def download_anime():
    episode_list = list()

    with open('anime_list.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            file_name = str(line.split('|')[0]).strip()
            url = line.split('|')[1]
            episode_list.append([file_name, url])

    for episode in episode_list:
        file_name = episode[0]
        url = episode[1]
        print('filename = {}, url = {}'.format(file_name, url))

        save_download(file_name, url)

        time.sleep(1)


if __name__ == '__main__':

    max_retries = 5
    retry_delay = 1

    save_path = 'F://Video//Anime//new_anime//'

    driver = init_driver()

    if get_list_len == 0:
        flag = get_episode(driver=driver)
    else:
        download_anime()
