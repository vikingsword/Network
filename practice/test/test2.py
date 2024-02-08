# !usr/bin/env python
# -*- coding:utf-8 _*-
from selenium import webdriver

class Driver:

    def __init__(self):
        self.driver = webdriver.Edge()

    def get(self, url):
        self.driver.get(url)


if __name__ == '__main__':
    driver = Driver()
    driver.get('https://www.baidu.com')