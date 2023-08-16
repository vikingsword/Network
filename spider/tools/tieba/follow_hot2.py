'''
贴吧自动关注热门吧
'''

import os.path
import pickle
import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_option = Options()
# chrome_option.add_argument('--headless')
# chrome_option.add_argument('--disable-gpu')

# 规避检测
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])

s = Service(executable_path='../chromedriver.exe')
# browser对象 或者是 driver对象
driver = webdriver.Chrome(service=s, options=chrome_option)
# 最大化浏览器窗口
driver.maximize_window()

url = 'https://tieba.baidu.com/'


def save_cookie():
    driver.get(url)
    resp = driver.page_source
    tree = etree.HTML(resp)
    login_text = tree.xpath('//div[@class="u_menu_item"]/a/text()')[0]
    if login_text == '登录':
        # 未登录，需要登陆，登陆后持久化cookie
        div = driver.find_element(By.XPATH, '//div[@class="u_menu_item"]/a')
        div.click()
        print('请扫码登录')
        time.sleep(20)

        with open('cookie.pkl', 'wb') as file:
            pickle.dump(driver.get_cookies(), file)
            print('cookie 持久化完成')
        username = tree.xpath('//div[@class="u_menu_item"]/a/span/text()')
        if username is not None:
            print('登陆成功')
    else:
        print('用户已经登陆')


def add_cookies():
    while True:
        if os.path.exists('cookie.pkl'):
            with open('cookie.pkl', 'rb') as file:
                cookies = pickle.load(file)
            driver.get(url)
            for cookie in cookies:
                driver.add_cookie(cookie)
            time.sleep(1)

            driver.refresh()
            time.sleep(1)

            break
        else:
            save_cookie()


def get_follow_list():

    url_follow = 'https://tieba.baidu.com/i/i/forum'
    driver.get(url_follow)
    resp = driver.page_source
    tree = etree.HTML(resp)
    tr_list = tree.xpath('//div[@class="forum_table"]//tr')
    tieba_list = []
    for tr in tr_list:
        href_list = tr.xpath('./td[1]/a/@href')
        try:
            href = href_list[0]
            tieba_url = url + href
            tieba_list.append(tieba_url)
        except Exception as e:
            pass
    return tieba_list


def get_hot_list():
    # 一共198热门吧
    add_cookies()
    hot_list = list()
    if os.path.exists('hot_list.txt'):
        for hot in open('hot_list', 'r', encoding='utf-8'):
            if hot != '':
                hot = hot.strip()
                hot_list.append(hot)
    else:
        with open('hot_list.txt', 'a+', encoding='utf-8') as f:
            for page in range(1, 18):
                resp = driver.page_source
                tree = etree.HTML(resp)
                hrefs = tree.xpath('//div[@id="forum_rcmd"]//li[@class="rcmd_forum_item"]/a/@href')
                for href in hrefs:
                    hot_url = 'https://tieba.baidu.com' + str(href)
                    hot_list.append(hot_url)
                    f.write(hot_url + '\n')
                driver.find_element(By.ID, 'btnNextPage').click()
                time.sleep(0.5)
    f.close()
    return hot_list


def get_unfollow():
    all_hot_tieba = list()
    for url in open('hot_list.txt', 'r', encoding='utf-8'):
        url = url.strip()
        all_hot_tieba.append(url)
    your_follows = get_follow_list()

    unfollow_list = list()
    for url in all_hot_tieba:
        if url in your_follows:
            continue
        else:
            unfollow_list.append(url)
    return unfollow_list


def follow_tieba():
    unfollows = get_unfollow()
    for unfollow in unfollows:
        driver.get(unfollow)
        driver.find_element(By.ID, 'j_head_focus_btn').click()
        # 操作频繁，无法继续关注，休息下
        time.sleep(2)
        # print(hot_url)


if __name__ == '__main__':
    follow_tieba()
