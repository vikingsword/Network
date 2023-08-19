import json
import os.path
import pickle
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_option = Options()
# 无头浏览器
# chrome_option.add_argument('--headless')
# chrome_option.add_argument('--disable-gpu')

# 规避检测
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])

s = Service(executable_path='../../chromedriver.exe')

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
    driver.implicitly_wait(1)

    driver.find_element(By.ID, 'email1').send_keys(username)
    driver.find_element(By.ID, 'password1').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="appCapsule"]/div[1]/div/div[2]/formsss/button').click()
    driver.implicitly_wait(1)


def demo():
    login()
    # 创建一个显式等待，等待直到元素可见
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="homecontentbox"]/div/div/div[2]/div/label[1]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="homecontentbox"]/div/div/div[2]/div/label[1]'))).click()

    # accept cookies
    driver.find_element(By.XPATH, '//div[@class="appBottomMenu"]/a[2]').click()


if __name__ == '__main__':

    demo()

    input()
