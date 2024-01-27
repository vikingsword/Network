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

# 切换到第一个 iframe，你可以根据实际情况修改索引或使用其他定位方法
iframe_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
)
driver.switch_to.frame(iframe_element)

# 切换到包含新的 <html> 的 iframe，同样你需要根据实际情况修改定位方法
second_iframe_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'html'))
)
driver.switch_to.frame(second_iframe_element)

# 在新的 <html> 中执行操作，例如获取源码
new_html_page_source = driver.page_source

# 打印新的 <html> 中的源码
print(new_html_page_source)
