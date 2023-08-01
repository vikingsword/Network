import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='../chromedriver.exe')
bro = webdriver.Chrome(service=s)
# 一定要写完整路径
bro.get('https://www.biquge7.xyz/ph')
page_text = bro.page_source
tree = etree.HTML(page_text)
title_list = tree.xpath('//div[@class="tui"]//div[@class="title"]/a/text()')

count = 0
for title in title_list:
    print(title)
    count += 1
time.sleep(2)
# 实际上不用关闭, 系统自动清除内存
bro.quit()
print(count)