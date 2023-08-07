import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')

# 规避检测
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])

s = Service(executable_path='chromedriver.exe')
bro = webdriver.Chrome(service=s, options=chrome_option)

url = 'https://www.bilibili.com'
bro.get(url)
page_source = bro.page_source
tree = etree.HTML(page_source)
title_list = tree.xpath('//div[@class="feed2"]//h3[@class="bili-video-card__info--tit"]/@title')
for title in title_list:
    print(title)

input()
bro.quit()
