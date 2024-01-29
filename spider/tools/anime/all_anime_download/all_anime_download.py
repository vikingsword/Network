# !usr/bin/env python
# -*- coding:utf-8 _*-
import os.path
import time
from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests


def init_driver():
    edge_option = webdriver.EdgeOptions()
    edge_option.add_argument('--headless')
    edge_option.add_argument('--gpu-disable')
    edge_option.add_argument('--mute-audio')
    driver = webdriver.Edge(options=edge_option)
    driver.implicitly_wait(30)
    return driver


def get_page_urls(driver):
    base_url = 'https://www.ntdm9.com'
    download_list = list()
    with open('anime_homepage.txt', 'r', encoding='utf-8') as f:
        for url in f:
            url = url.strip()
            driver.get(url)
            page_source = driver.page_source
            # get anime title
            tree1 = etree.HTML(page_source)
            anime_title = tree1.xpath('//div[@class="blockcontent"]//h4[@class="detail_imform_name"]/text()')[0]
            # get every episode url
            tree2 = etree.HTML(page_source)
            # 指定li标签的范围： //ul/li[position() >= 100 and position() <= 200]
            li_list = tree2.xpath('//div[@id="main0"]//ul/li')
            episode_urls = list()
            for li in li_list:
                href = li.xpath('./a/@href')[0]
                episode_url = base_url + href
                episode_urls.append(episode_url)
            # 将 动漫名和该动漫每一页的list作为一个元组放入 download_list 中
            download_list.append([anime_title, episode_urls])
        return download_list


def download_anime(list):
    driver = init_driver()
    for item in list:
        dir_path = save_path + item[0] + "//"
        is_exists = os.path.exists(dir_path)
        if not is_exists:
            os.makedirs(dir_path)
        print("path = ", dir_path)
        # 下载动漫的每一集
        for url in item[1]:
            driver.get(url)
            # 获取每一集的标题
            episode_title = driver.title
            file_name = dir_path + episode_title + ".mp4"
            print("filename = ", file_name)
            # 开始下载每集
            save_download(file_name, url)
            time.sleep(1)


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


def download_handler(filename, url):
    driver2 = init_driver()
    driver2.get(url)
    print("url = ", url)
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


def download_detail(filename, url):
    try:
        print('开始下载： ', filename.split('//')[-1] + " ......")
        # 发送 GET 请求获取视频文件
        response = requests.get(url, stream=True)

        # 检查请求是否成功
        response.raise_for_status()

        # 以二进制写入文件
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Video downloaded successfully to: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading video: {e}")


if __name__ == '__main__':
    max_retries = 5
    retry_delay = 1

    save_path = 'F://Video//Anime//'

    driver = init_driver()
    info_list = get_page_urls(driver)
    download_anime(info_list)
