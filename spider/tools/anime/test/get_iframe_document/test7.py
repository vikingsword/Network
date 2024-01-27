# !usr/bin/env python
# -*- coding:utf-8 _*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.ntdm9.com/play/5534-1-4.html'

driver = webdriver.Edge()

driver.implicitly_wait(30)

driver.get(url)
element = driver.find_element(By.XPATH, '//div[@id="ageframediv"]//div[@class="MacPlayer"]//table//td[@id="playleft"]')
print(element)



driver.close()
