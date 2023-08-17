'''
贴吧自动签到脚本
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

s = Service(executable_path='../../chromedriver.exe')
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

        with open('../cookie.pkl', 'wb') as file:
            pickle.dump(driver.get_cookies(), file)
            print('cookie 持久化完成')
        username = tree.xpath('//div[@class="u_menu_item"]/a/span/text()')
        if username is not None:
            print('登陆成功')
    else:
        print('用户已经登陆')


def add_cookies():
    while True:
        if os.path.exists('../cookie.pkl'):
            with open('../cookie.pkl', 'rb') as file:
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


def get_hot_list():
    # 一共198热门吧
    add_cookies()
    hot_list = []
    for page in range(1, 18):
        resp = driver.page_source
        tree = etree.HTML(resp)
        hrefs = tree.xpath('//div[@id="forum_rcmd"]//li[@class="rcmd_forum_item"]/a/@href')
        for href in hrefs:
            hot_url = 'https://tieba.baidu.com' + str(href)
            hot_list.append(hot_url)
        driver.find_element(By.ID, 'btnNextPage').click()
        time.sleep(0.5)
    return hot_list


def follow_hot_tieba():
    hots = get_hot_list()
    for hot_url in hots:
        driver.get(hot_url)
        driver.find_element(By.ID, 'j_head_focus_btn').click()
        # 操作频繁，无法继续关注，休息下
        time.sleep(2)
        # print(hot_url)


if __name__ == '__main__':
    follow_hot_tieba()
