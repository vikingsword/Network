import time
from selenium import webdriver
# 动作链
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# todo 滑动验证如何绕过
s = Service(executable_path='../chromedriver.exe')
bro = webdriver.Chrome(service=s)

url = 'https://qzone.qq.com/'
bro.get(url)
bro.switch_to.frame('login_frame')
a_tag = bro.find_element(By.ID, 'switcher_plogin')
a_tag.click()

# action = ActionChains(bro)
# action.click()
uname = bro.find_element(By.ID, 'u').send_keys('1974392477')
upass = bro.find_element(By.ID, 'p').send_keys('123456')
time.sleep(1)

button = bro.find_element(By.ID, 'login_button')
button.click()
time.sleep(3)

div = bro.find_element(By.CLASS_NAME, 'tc-slider-bg')
action = ActionChains(bro)
action.click_and_hold(div)
time.sleep(5)
action.drag_and_drop_by_offset(div, 150, 0).perform()
time.sleep(2)
action.release().perform()

time.sleep(3)
bro.quit()
