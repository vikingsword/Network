import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("headless")

# driver = webdriver.Edge(options=options)

driver = webdriver.Edge()

base_url = 'https://www.dangdang.com'
driver.get(base_url)
js = "window.scrollTo(0,10000)"
driver.execute_script(js)

time.sleep(3)
driver.close()