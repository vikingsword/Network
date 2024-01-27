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
driver.get(url)
driver.maximize_window()

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

# 等待视频元素加载完成
video_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'video'))
)
# 获取视频文件地址
video_source = video_element.get_attribute('src')
# 打印视频文件地址
print(f"Video source: {video_source}")

input()
driver.close()
