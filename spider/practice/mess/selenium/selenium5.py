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

with open('cookie.pkl', 'wb') as file:
    pickle.dump(driver.get_cookies(), file)

driver.get(url)
resp = driver.page_source
tree = etree.HTML(resp)
login_text = tree.xpath('//div[@class="u_menu_item"]/a/text()')[0]
if login_text == '登录':
    # 未登录，需要登陆，登陆后持久化cookie
    div = driver.find_element(By.XPATH, '//div[@class="u_menu_item"]/a')
    div.click()
    print('请扫码登录')
    time.sleep(20)

    with open('cookie.pkl', 'wb') as file:
        pickle.dump(driver.get_cookies(), file)
        print('cookie 持久化完成')
    username = tree.xpath('//div[@class="u_menu_item"]/a/span/text()')
    if username is not None:
        print('登陆成功')

else:
    print('登录成功')
input()

driver.quit()
