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

driver.get(url)

time.sleep(5)
page_source = driver.page_source
print(page_source)

input()
driver.close()
