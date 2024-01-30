# -*- coding: utf-8 -*-
import time

from selenium import webdriver

from action.reply_a_post import reply_a_post
from login import login

if __name__ == '__main__':
    url = 'https://tieba.baidu.com/'
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get(url)

    # 登录
    login(driver)

    content = 'hello3'
    post_url = 'https://tieba.baidu.com/p/8875880579'
    reply_a_post(driver, post_url, content)

    time.sleep(20)
    # 防止自动退出
    input()
    driver.close()


