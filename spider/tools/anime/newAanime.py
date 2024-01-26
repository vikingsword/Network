# !usr/bin/env python
# -*- coding:utf-8 _*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree

url = 'https://www.ntdm9.com/play/5534-1-4.html'

# no headers
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--headless")
driver = webdriver.Edge(options=edge_options)
driver.implicitly_wait(30)

driver.get(url)
page_source = driver.page_source

tree = etree.HTML(page_source)

element = driver.find_element(By.TAG_NAME, 'video').get_attribute('src')
print(element)

time.sleep(10)
driver.close()
