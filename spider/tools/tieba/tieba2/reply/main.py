# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from action.reply_content import reply_text
from action.reply_content import reply_img
from login import login

if __name__ == '__main__':
    url = 'https://tieba.baidu.com/'
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get(url)

    # 登录
    login(driver)

    # # 发送文本
    # content = 'hello3'
    # post_url = 'https://tieba.baidu.com/p/8875880579'
    # reply_text(driver, post_url, content)

    # 发送图片
    post_url = 'https://tieba.baidu.com/p/8875880579'
    reply_img(driver, post_url)


    time.sleep(20)
    # 防止自动退出
    input()
    driver.close()
