from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('https://baidu.com')

element = driver.find_element(By.ID, 'kw')
element.send_keys('selenium')
element.submit()

time.sleep(5)
driver.quit()