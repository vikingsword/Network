import json
import os.path
import pickle

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_option = Options()
# 无头浏览器
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')

# 规避检测
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])

s = Service(executable_path='../../../chromedriver.exe')

# get browser object
driver = webdriver.Chrome(service=s, options=chrome_option)
# maximize browser
driver.maximize_window()

username = 'vikingar'
password = 'Wsh!19749188'


def login():
    url_login = 'http://manhuabika.com/plogin/'
    driver.get(url_login)
    # 等待登录页面加载完毕
    wait = WebDriverWait(driver, 3)

    driver.find_element(By.ID, 'email1').send_keys(username)
    driver.find_element(By.ID, 'password1').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="appCapsule"]/div[1]/div/div[2]/formsss/button').click()
    driver.implicitly_wait(3)

    driver.get('http://manhuabika.com/phome')
    driver.refresh()
    token = driver.execute_script(
        "return window.localStorage.getItem('token');"
    )
    print(token)
    if os.path.exists('authorization.pkl'):
        pass
    else:
        with open('./authorization.pkl', 'wb') as f:
            pickle.dump(token, f)
            print('cookie saved !')
        print('login success!')


if __name__ == '__main__':
    try:
        login()
    except Exception as e:
        pass

    input()
