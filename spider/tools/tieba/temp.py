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

    add_cookies()
    url_follow = 'https://tieba.baidu.com/i/i/forum'
    driver.get(url_follow)
    resp = driver.page_source
    tree = etree.HTML(resp)

    while True:
        next_page = driver.find_element(By.XPATH, '//div[@id="j_pagebar"]/div/a[3]')
        follow_list = list()
        if next_page.text == '下一页':
            tr_list = tree.xpath('//div[@class="forum_table"]//tr')
            for tr in tr_list:
                href_list = tr.xpath('./td[1]/a/@href')
                try:
                    href = href_list[0]
                    tieba_url = url + href
                    follow_list.append(tieba_url)
                    next_page.click()
                    time.sleep(0.5)
                except Exception as e:
                    pass
        else:
            return follow_list


if __name__ == '__main__':
    follow_list = get_follow_list()
    for follow in follow_list:
        print(follow)

