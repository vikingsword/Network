# !usr/bin/env python
# -*- coding:utf-8 _*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.ntdm9.com/play/5534-1-4.html'
edge_option = webdriver.EdgeOptions()
edge_option.add_argument('--headless')
edge_option.add_argument('--gpu-disable')
driver = webdriver.Edge(options=edge_option)
driver.implicitly_wait(30)

driver.get(url)

driver.switch_to.frame('buffer')
# element = driver.find_element(By.XPATH, '//div[@id="ageframediv"]//div[@class="MacPlayer"]//*id[@id="playleft"]//iframe/@src')
# element = driver.find_element(By.ID, 'playleft')
element = driver.find_element(By.CLASS_NAME, 'MacPlayer')
# driver.execute_script(
#     'return document.getElementById("buffer").contentWindow.document.getElementsByTagName("video")[0].src')
print(element)


input()
driver.close()