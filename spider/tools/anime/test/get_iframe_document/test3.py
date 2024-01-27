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

driver.maximize_window()

# 打开网站
driver.get(url)

# 切换到第一个 iframe，你可以根据实际情况修改索引或使用其他定位方法
first_iframe_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
)
driver.switch_to.frame(first_iframe_element)

# 切换到包含 #document 的 iframe
document_iframe_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#document'))
)
driver.switch_to.frame(document_iframe_element)

# 在 #document 中执行操作，例如获取源码
document_page_source = driver.page_source

# 打印 #document 中的源码
print(document_page_source)
input()
driver.close()
