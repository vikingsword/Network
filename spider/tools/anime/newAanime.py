# !usr/bin/env python
# -*- coding:utf-8 _*-
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree

url = 'https://www.ntdm9.com/play/5534-1-4.html'

# # no headers
# edge_options = webdriver.EdgeOptions()
# edge_options.add_argument("--headless")
# driver = webdriver.Edge(options=edge_options)

# headers
driver = webdriver.Edge()


driver.implicitly_wait(30)
driver.maximize_window()
driver.get(url)

# 获取浏览器窗口的大小
window_size = driver.get_window_size()

# 设置要点击的位置（这里以浏览器窗口中心为例）
click_x, click_y = window_size['width'] // 2, window_size['height'] // 2

# 创建 ActionChains 对象
actions = ActionChains(driver)

# 移动到浏览器窗口的特定位置并点击
actions.move_by_offset(click_x, click_y)
time.sleep(3)
actions.click()
actions.perform()

driver.execute_script("return jQuery.active == 0")  # 适用于页面中使用 jQuery

page_source = driver.page_source
with open('page_source.txt', 'w', encoding='utf-8') as f:
    f.write(page_source)

input()
driver.close()
