import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='./chromedriver.exe')
bro = webdriver.Chrome(service=s)

bro.get('https://www.taobao.com/')

# 标签定位
search_input = bro.find_element(By.ID, value='q')
# 标签交互
search_input.send_keys('cheese')

# 执行js代码
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(5)
# 按钮点击
button = bro.find_element(By.CSS_SELECTOR, value='.btn-search')
button.click()

bro.get('https://www.baidu.com')
time.sleep(2)
bro.back()
time.sleep(2)
bro.forward()

time.sleep(2)
bro.quit()