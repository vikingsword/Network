import os.path
import pickle
import time

import requests
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

s = Service(executable_path='../../../chromedriver.exe')
# browser对象 或者是 driver对象
driver = webdriver.Chrome(service=s, options=chrome_option)
# 最大化浏览器窗口
driver.maximize_window()

url = 'https://tieba.baidu.com'


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


def demo_follow():
    page_num = 0
    add_cookies()
    url_follow = 'https://tieba.baidu.com/i/i/forum'
    # 获取页码
    driver.get(url_follow)
    driver.find_element(By.CLASS_NAME, 'pm_i_know').click()
    driver.implicitly_wait(1)
    try:
        last_a = driver.find_elements(By.XPATH, '//div[@id="j_pagebar"]//a')[-1]
        page_num = last_a.get_attribute('href').split('=')[-1]
    except Exception as e:
        pass
    # print(page_num)
    url_follow_page = 'https://tieba.baidu.com/i/i/forum?&pn='
    tieba_list = list()
    for page in range(1, int(page_num) + 1):
        page_url = url_follow_page + str(page)
        driver.get(page_url)
        resp = driver.page_source
        tree = etree.HTML(resp)
        tr_list = tree.xpath('//div[@class="forum_table"]//tr')

        for tr in tr_list:
            href_list = tr.xpath('./td[1]/a/@href')
            try:
                href = href_list[0]
                tieba_url = url + href
                tieba_list.append(tieba_url)
            except Exception as e:
                pass
    return tieba_list


if __name__ == '__main__':
    list = demo_follow()
    for item in list:
        print(item)
    input()
