# !usr/bin/env python
# -*- coding:utf-8 _*-
from selenium import webdriver


def init_driver():
    edge_option = webdriver.EdgeOptions()
    edge_option.add_argument('--headless')
    edge_option.add_argument('--gpu-disable')
    driver = webdriver.Edge(options=edge_option)
    driver.implicitly_wait(30)
    return driver





if __name__ == '__main__':
    driver = init_driver()
