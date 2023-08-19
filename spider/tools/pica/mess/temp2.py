import os.path
import pickle

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

chrome_option = Options()

chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])

s = Service(executable_path='../../chromedriver.exe')

driver = webdriver.Chrome(service=s, options=chrome_option)

if os.path.exists('cookie.pkl'):
    with open('cookie.pkl', 'rb') as f:
        cookies = pickle.load(f)
else:
    print('cookie is not exist! ')


url = 'http://manhuabika.com/phome/'
driver.get(url)
for cookie in cookies:
    driver.add_cookie(cookie)

input()
