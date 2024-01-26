# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from login import login



if __name__ == '__main__':
    url = 'https://tieba.baidu.com/'
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get(url)

    # 登录
    login(driver)

    post_url = 'https://tieba.baidu.com/p/8875880579'
    driver.get(post_url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//div[@id="rich_ueditor_tpl"]//div[@class="old_style_wrapper"]')
    action = ActionChains(driver)
    action.move_to_element_with_offset(element, 50, 50)
    action.click()
    action.send_keys('hello2')
    action.perform()

    element2 = driver.find_element(By.XPATH, '//div[@id="tb_rich_poster"]//div[@class="j_floating"]//span')
    action.move_to_element_with_offset(element2, 3, 3)
    action.click()
    action.perform()


    time.sleep(30)
    # 防止自动退出
    input()
    driver.close()
