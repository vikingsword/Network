from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.get_cookie())


# input = driver.find_element_by_id('#kw')
# input.send_keys("valley")
#
# button = driver.find_element_by_css_selector('#su')
# button.click()
