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
td_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//table//td[@id="playleft"]'))
)

# 在 td 元素下找到 iframe 元素
iframe_element = td_element.find_element(By.TAG_NAME, 'iframe')

# 切换到 iframe
driver.switch_to.frame(iframe_element)

# 在 iframe 中执行操作，例如获取源码
# 这里获取到的源码就是上面 iframe 下面 document中的
iframe_page_source = driver.page_source

# 获取 page_source 中的 video 标签
tree = etree.HTML(iframe_page_source)
anime_src = tree.xpath('//video[@id="lelevideo"]/@src')[0]
print(anime_src)

# 打印 iframe 中的源码
# print(iframe_page_source)

driver.close()
