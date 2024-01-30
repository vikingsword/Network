# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def reply_a_post(driver, url, content):
    post_url = url
    driver.get(post_url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # 点击回复框
    element = driver.find_element(By.XPATH, '//div[@id="rich_ueditor_tpl"]//div[@class="old_style_wrapper"]')
    action = ActionChains(driver)
    action.move_to_element_with_offset(element, 50, 50)
    action.click()
    action.send_keys(content)
    action.perform()

    # 点击发表 reply post
    element2 = driver.find_element(By.XPATH, '//div[@id="tb_rich_poster"]//div[@class="j_floating"]//span')
    action.move_to_element_with_offset(element2, 3, 3)
    action.click()
    action.perform()