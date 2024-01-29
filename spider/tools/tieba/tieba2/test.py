# !usr/bin/env python
# -*- coding:utf-8 _*-
import os.path
import time
from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests


def init_driver():
    edge_option = webdriver.EdgeOptions()
    edge_option.add_argument('--headless')
    edge_option.add_argument('--gpu-disable')
    edge_option.add_argument('--mute-audio')
    driver = webdriver.Edge(options=edge_option)
    driver.implicitly_wait(30)
    return driver