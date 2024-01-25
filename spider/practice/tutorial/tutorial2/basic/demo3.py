import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.chrome.options import Options

base_url = 'https://www.dangdang.com'
driver = webdriver.Edge()
# 全局隐式等待20s
driver.implicitly_wait(20)

# without headers
# 创建Edge选项对象
edge_options = Options()

# 启用无头模式
edge_options.add_argument('--headless')
edge_options.add_argument('--disable-gpu')

driver.get(base_url)

element = driver.find_element(By.ID, 'key_S')
element.send_keys('科幻')
element.submit()

page_source = driver.page_source
tree = etree.HTML(page_source)

# get total page
url_list= []
# https://search.dangdang.com
search_base_url = base_url.replace('www', 'search')
total_page = str(tree.xpath('//div[@class="paging"]/ul//li[9]/a/@href')[0]).split('=')[-1]
# https://search.dangdang.com/?key=%BF%C6%BB%C3&act=input&page_index=
url_without_page = search_base_url +str(tree.xpath('//div[@class="paging"]/ul//li[9]/a/@href')[0]).replace(total_page, '')

# get all book info
title_list = []
with open('./price.txt', 'a+', encoding='utf-8') as f:

    for page in range(1, int(total_page) + 1):
        target_url = url_without_page + str(page)
        driver.get(target_url)

        # get all title
        page_source = driver.page_source
        tree = etree.HTML(page_source)
        li_list = tree.xpath('//div[@id="search_nature_rg"]/ul/li')
        # 每个 li 标签是一本书
        for li in li_list:
            title = str(li.xpath('./a/@title')[0]).replace(' ', '')
            price = str(li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()')[0])
            f.write(price + '\n')


time.sleep(3)
driver.close()
