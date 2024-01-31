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
# driver.maximize_window()

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

        with open('undo/cookie.pkl', 'wb') as file:
            pickle.dump(driver.get_cookies(), file)
            print('cookie 持久化完成')
        username = tree.xpath('//div[@class="u_menu_item"]/a/span/text()')
        if username is not None:
            print('登陆成功')
    else:
        print('用户已经登陆')


def get_tieba_list():
    while True:
        if os.path.exists('undo/cookie.pkl'):
            with open('undo/cookie.pkl', 'rb') as file:
                cookies = pickle.load(file)
            break
        else:
            save_cookie()

    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(2)

    driver.refresh()

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


def sign_in():
    tieba_list = get_tieba_list()
    for tieba in tieba_list:
        # print(tieba)
        driver.get(tieba)
        driver.maximize_window()
        time.sleep(0.2)

        div = driver.find_element(By.ID, 'signstar_wrapper')
        div.click()
        time.sleep(0.3)
    input()

    driver.quit()


if __name__ == '__main__':
    sign_in()
