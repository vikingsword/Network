import pickle
import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_option = Options()
# chrome_option.add_argument('--headless')
# chrome_option.add_argument('--disable-gpu')

# 规避检测
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])

s = Service(executable_path='./chromedriver.exe')
bro = webdriver.Chrome(service=s, options=chrome_option)

url = 'https://www.bilibili.com'
bro.get(url)

# """假如说我现在本地有 cookies.pkl 那么 直接获取"""
# cookies = pickle.load(open('cookies.pkl', 'rb'))
# for cookie in cookies:
#     cookie_dict = {
#         'domain': '.damai.cn',  # 必须要有的, 否则就是假登录
#         'name': cookie.get('name'),
#         'value': cookie.get('value')
#     }
#     bro.add_cookie(cookie_dict)
# print('###载入cookie###')

page_source = bro.page_source
tree = etree.HTML(page_source)
div = tree.xpath('//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div/span')
bro.find_element(By.CLASS_NAME, 'header-login-entry').click()
print('##### 请扫码登陆 #####')
while True:
    try:
        user_div = bro.find_element(By.CLASS_NAME, 'bili-avatar-pendent-dom')
        if user_div is not None:
            print('##### 登陆成功 #####')
            pickle.dump(bro.get_cookies(), open('cookies.pkl', 'wb'))
            print('###cookie保存成功###')
            break
        else:
            time.sleep(3)
    except Exception as e:
        pass

time.sleep(2)
user_info = bro.find_element(By.CLASS_NAME, 'bili-avatar').click()
time.sleep(1)

first_window_handle = bro.current_window_handle

window_handles = bro.window_handles
new_window_handle = None
for handle in window_handles:
    if handle != first_window_handle:
        new_window_handle = handle
        break

bro.switch_to.window(new_window_handle)
# my_follow = bro.find_element(By.ID, 'n-gz').click()

input()
bro.quit()
