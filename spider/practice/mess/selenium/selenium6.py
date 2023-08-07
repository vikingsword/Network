import pickle
import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_option = Options()
# chrome_option.add_argument('--headless')
# chrome_option.add_argument('--disable-gpu')

# 规避检测
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])

s = Service(executable_path='chromedriver.exe')
# browser对象 或者是 driver对象
driver = webdriver.Chrome(service=s, options=chrome_option)

url = 'https://tieba.baidu.com/'

with open('cookie.pkl', 'rb') as file:
    cookies = pickle.load(file)

driver.get(url)
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(2)

driver.refresh()

input()

driver.quit()
