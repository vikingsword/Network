import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='chromedriver.exe')
bro = webdriver.Chrome(service=s)

bro.get('https://www.bilibili.com')

page_source = bro.page_source
tree = etree.HTML(page_source)
title_list = tree.xpath('//div[@class="feed2"]//h3[@class="bili-video-card__info--tit"]/@title')
for title in title_list:
    print(title)

input()
bro.quit()
