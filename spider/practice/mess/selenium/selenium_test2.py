import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='chromedriver.exe')
bro = webdriver.Chrome(service=s)

bro.get('https://www.bilibili.com')


first_window_handle = bro.current_window_handle
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')

search_input = bro.find_element(By.CLASS_NAME, 'nav-search-input')
search_input.send_keys('hello')
time.sleep(2)

button = bro.find_element(By.CLASS_NAME, 'nav-search-btn')
button.click()

window_handles = bro.window_handles
new_window_handle = None
for handle in window_handles:
    if handle != first_window_handle:
        new_window_handle = handle
        break

bro.switch_to.window(new_window_handle)
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(2)

input()
bro.quit()
