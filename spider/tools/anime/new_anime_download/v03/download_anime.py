# !usr/bin/env python
# -*- coding:utf-8 _*-
import os.path
import time
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
    edge_option.add_argument('--mute-audio')
    driver = webdriver.Edge(options=edge_option)
    driver.implicitly_wait(30)
    return driver


def download_detail(filename, url):
    try:
        # 发送 GET 请求获取视频文件
        print('start download file ', filename)
        response = requests.head(url, stream=True)

        # 检查请求是否成功
        response.raise_for_status()

        bytes_size = int(response.headers.get('content-length', 0))

        # 以二进制写入文件
        path = save_path + filename + ".mp4"
        with open(path, 'wb') as file, tqdm(
            desc=filename,
            total=bytes_size,
            unit='B',
            unit_scale=True,
            unit_divisor=8192,
            colour='#0396ff'
        ) as bar:
            response = requests.get(url, stream=True)
            for data in response.iter_content(chunk_size=8192):
                bar.update(len(data))
                file.write(data)
        print(f"Video downloaded successfully to: {path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading video: {e}")


def download_handler(filename, url):
    driver2 = init_driver()
    driver2.get(url)
    print("url_ = ", url)
    td_element = WebDriverWait(driver2, 30).until(
        EC.presence_of_element_located((By.XPATH, '//table//td[@id="playleft"]'))
    )

    iframe_element = td_element.find_element(By.TAG_NAME, 'iframe')

    driver2.switch_to.frame(iframe_element)
    iframe_page_source = driver2.page_source
    tree = etree.HTML(iframe_page_source)
    anime_src = tree.xpath('//video[@id="lelevideo"]/@src')[0]
    print("anime_src = ", anime_src)
    download_detail(filename, anime_src)


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
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    driver = init_driver()

    flag = get_episode(driver=driver)
    if flag:
        download_anime()
