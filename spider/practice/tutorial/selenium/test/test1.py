from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = 'http://www.python.org'
driver = webdriver.Edge()
driver.get(url)
time.sleep(10)
driver.close()