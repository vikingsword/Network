import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://fanyi.youdao.com/index.html#/'

driver = webdriver.Edge()
driver.get(url)
driver.maximize_window()

time.sleep(2)
driver.refresh()



# close_button = driver.find_element(By.XPATH, '//div[@class="inner-content"]//div[@class="close"]')
# close_button.click()


# page_text = driver.page_source
# tree = etree.HTML(page_text)
# close_button = tree.xpath('//div[@class="inner-content"]//div[@class="close"]')


time.sleep(100)
driver.close()