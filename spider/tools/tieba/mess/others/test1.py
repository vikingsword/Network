# !usr/bin/env python
# -*- coding:utf-8 _*-
# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import logging
import sys
import random
import uuid
from pywinauto import Application
from pywinauto.keyboard import send_keys

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', filemode='w',
                    filename="log.txt")
BROWSER_URL = r'D:\program files (x86)\360chrome\Chrome\Application\360chrome.exe'

from pywinauto.application import Application


class WinAuto:

    def __init__(self, class_name, title_re):
        # 连接到指定应用程序，此处为连接到指定窗口
        self.app = Application().connect(class_name=class_name, title_re=title_re)

    # 定位窗口方法
    def get_window(self, window_object, class_name="", title_re=""):
        return window_object.window(class_name=class_name, title_re=title_re)

    # 向编辑框输入指定信息
    def file_input(self, file_path):
        # 定位到标题名为“打开”对话框
        window = self.get_window(self.app, "#32770", "打开")
        # 定位到编辑框
        window = self.get_window(window, class_name="Edit")
        # 向编辑框中输入信息
        window.TypeKeys(file_path)

    # 点击【打开】按钮
    def open_button_click(self):
        # 定位到标题名为“打开”对话框
        window = self.get_window(self.app, "#32770", "打开")
        # 定位到【打开】按钮
        button = self.get_window(window, class_name="Button", title_re="打开")
        # 点击【打开】按钮
        button.click()


def get_titile():
    title_list = [
        "双十一最强攻略，保证有惊喜，进来了解一下吧",
        "双十一撸货套路，来了解一下",
        "双11无敌神车已经发车，来了解一下把",
        "双11最强攻略，保证你不后悔",
        "双十一最强攻略，走过路过不要错过",
    ]
    t = random.choice(title_list)
    return t + str(uuid.uuid4()).split('-')[-1]


def get_content():
    content = """testest{uuid}atetset{uuid}testest{uuid}test""".format(uuid=str(uuid.uuid4()).split('-')[-1])

    return content


def get_datas():
    with open('tieba.txt', 'r', encoding='utf-8', errors='ignore') as fp:
        schools = fp.readlines()
    title = get_titile()
    content = get_content()
    return title, content, schools


def get_sleep_time(num):
    if num % 5 == 0:
        t = random.choice(range(180, 300))
    else:
        t = random.choice(range(35, 125))
    logging.info("sleep {}".format(t))
    return t


def start_chrome():
    chrome_options = Options()
    chrome_options.binary_location = BROWSER_URL
    # chrome_options.add_argument("–incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    if login_tieba(driver):
        title, content, schools = get_datas()
        num = 0
        for name in schools:
            url = u"https://tieba.baidu.com/f?ie=utf-8&kw=%s&fr=search" % name
            logging.info("start request {}, url:{}".format(name, url))
            try:
                driver.get(url)
            except Exception as e:
                logging.error("request {} error".format(name))
                continue
            followers = driver.find_element_by_class_name("card_menNum").text
            logging.info("followers is :{}".format(followers))
            followers = followers.replace(',', "")
            if int(followers) < 50000:
                logging.info("Less than 50000 followers")
                continue
            try:
                driver.find_element_by_xpath("/html/body/ul/li[2]/a").click()
                sleep(1)
                driver.find_element_by_xpath('//*[@id="tb_rich_poster"]/div[3]/div[1]/div[2]/input').send_keys(title)
                # driver.quit()
                sleep(1)
                driver.find_element_by_id("ueditor_replace").send_keys(content)
                sleep(1)
                driver.find_element_by_class_name('edui-btn-image').click()
                sleep(1)
                driver.find_element_by_class_name('pic_upload_container').click()
                sleep(1)
                driver.find_element_by_class_name('next_step').click()
                sleep(1)
                # 定位打开窗口
                window = WinAuto("#32770", "打开")
                sleep(1)
                if num % 2 == 0:
                    window.file_input(r'F:\py_home\selenium_auto\2.jpg')
                else:
                    window.file_input(r'F:\py_home\selenium_auto\3.jpg')
                sleep(1)
                window.open_button_click()
                sleep(8)
                driver.find_element_by_link_text('插入图片').click()
                sleep(5)
                driver.find_element_by_xpath('//*[@id="tb_rich_poster"]/div[3]/div[5]/div/button[1]').click()
            except Exception as e:
                logging.error("post article failed,: {}".format(e))
                import traceback
                traceback.print_exc()
                continue
            num += 1
            t = get_sleep_time(num)
            sleep(t)
    driver.quit()


def login_tieba(driver):
    tieba_url = 'https://tieba.baidu.com/'
    driver.get(tieba_url)
    driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()
    sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]').send_keys('用户名')
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]').send_keys('密码')
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submitWrapper"]').click()
        logging.info("login success")
    except Exception:
        logging.error("login failed")
        sys.exit(1)
    logging.info("wait for 10s")
    sleep(10)
    return True


if __name__ == '__main__':
    start_chrome()
