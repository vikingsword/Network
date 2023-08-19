import json
import os.path
import pickle

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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


def demo():
    url = 'http://manhuabika.com/phome/'
    driver.get(url)
    with open('authorization.pkl', 'rb') as f:
        cookie = pickle.load(f)
    authorization = json.loads(cookie)["value"]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Authorization': authorization
    }
    for key, value in headers.items():
        chrome_option.add_argument(f'--header={key}:{value}')

    driver.find_element(By.XPATH, '//*[@id="homecontentbox"]/div[@class="btn-group"]/label[1]').click()


if __name__ == '__main__':
    try:
        demo()
    except Exception as e:
        pass
    input()
