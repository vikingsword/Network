import time
from selenium import webdriver
# 动作链
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
# 实现无可视化界面
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实现规避检测
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

s = Service(executable_path='../chromedriver.exe')
bro = webdriver.Chrome(service=s, options=chrome_options)

# 无可视化界面(无头浏览器)
url = 'https://www.baidu.com'
bro.get(url)

print(bro.page_source)

bro.quit()
