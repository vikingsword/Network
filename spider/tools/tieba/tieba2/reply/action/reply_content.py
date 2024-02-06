# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def reply_text(driver, url, content):
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

    # 点击发表 reply text post
    element2 = driver.find_element(By.XPATH, '//div[@id="tb_rich_poster"]//div[@class="j_floating"]//span')
    action.move_to_element_with_offset(element2, 3, 3)
    action.click()
    action.perform()


def reply_img(driver, url):
    post_url = url
    driver.get(post_url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # 插入图片
    element = driver.find_element(By.XPATH,
                                  '//div[@class="edui-btn-toolbar"]//div[@class="edui-btn edui-btn-image edui-btn-name-list"]//div[@class="edui-icon-image edui-icon"]')
    action = ActionChains(driver)
    action.move_to_element_with_offset(element, 1, 1)
    action.click()
    action.perform()

    # 点击上传本地文件
    page_source = driver.page_source
    print(page_source.encode('gbk'))


    # element2 = driver.find_element(By.XPATH,
    #                                '//div[@class="edui-popup-body"]//ul[@class="layer_btn_list clearfix"]//li[@class="from_upload"]//a[@class="pic_upload_container"]')
    # action2 = ActionChains(driver)
    # action2.move_to_element_with_offset(element2, 1, 1)
    # action2.click()
    # action.perform()
