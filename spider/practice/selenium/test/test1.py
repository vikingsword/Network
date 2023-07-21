from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
#
# driver2 = webdriver.PhantomJS()
# driver2.get('https://www.baidu.com')