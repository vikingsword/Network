# !usr/bin/env python
# -*- coding:utf-8 _*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree

url = 'https://www.ntdm9.com/play/5534-1-4.html'

driver = webdriver.Edge()

driver.implicitly_wait(30)

driver.get(url)


# 使用 XPath 定位包含 iframe 的 td 元素
td_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//table//td[@id="playleft"]'))
)

# 在 td 元素下找到 iframe 元素
iframe_element = td_element.find_element(By.TAG_NAME, 'iframe')

# 切换到 iframe
driver.switch_to.frame(iframe_element)

# 在 iframe 中执行操作，例如获取源码
iframe_page_source = driver.page_source

# 打印 iframe 中的源码
print(iframe_page_source)