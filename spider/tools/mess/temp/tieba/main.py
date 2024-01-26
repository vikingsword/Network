import os
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
from selenium.webdriver.common.action_chains import ActionChains


# click login
def scan_login(tree):
    # 点击登录按钮
    div = driver.find_element(By.XPATH, '//div[@class="u_menu_item"]/a')
    div.click()
    print('请扫码登录')
    time.sleep(20)
    # 覆盖写入
    with open('./cookie.pkl', 'wb') as file:
        pickle.dump(driver.get_cookies(), file)
        print('cookie 持久化完成')
    username = tree.xpath('//div[@class="u_menu_item"]/a/span/text()')
    if username is not None:
        print('登陆成功')


def login_and_save_cookie():
    page_source = driver.page_source
    tree = etree.HTML(page_source)
    login_text = tree.xpath('//div[@class="u_menu_item"]/a/text()')[0]
    if login_text == '登录':
        # 未登录，需要登陆，登陆后持久化cookie
        # 先看之前是否保存过 cookie，如果有就读取，cookie可能过期
        if os.path.exists('./cookie.pkl'):
            with open('./cookie.pkl', 'rb') as file:
                cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
            print('加载cookie成功')
            # 查看 cookie 是否失效，如果失效，再get这个url也不显示登录按钮，需要重新扫码登录
            driver.get(url)
            page_source = driver.page_source
            tree = etree.HTML(page_source)
            login_text2 = tree.xpath('//div[@class="my_tieba_mod"]/h4/text()')
            # cookie 失效的情况
            if login_text2 is None:
                print('cookie 失效，请重新扫码登录')
                scan_login(tree)
        else:
            # 没有cookie，需要扫码登录
            scan_login(tree)
    else:
        print('用户登陆成功')


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/'
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get(url)
    time.sleep(3)
    driver.refresh()

    # 登录
    login_and_save_cookie()

    post_url = 'https://tieba.baidu.com/p/8875880579'
    driver.get(post_url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//div[@id="rich_ueditor_tpl"]//div[@class="old_style_wrapper"]')
    action = ActionChains(driver)
    action.move_to_element_with_offset(element, 50, 50)
    action.click()
    action.send_keys('hello')
    action.perform()

    element2 = driver.find_element(By.XPATH, '//div[@id="tb_rich_poster"]//div[@class="j_floating"]//span')
    action.move_to_element_with_offset(element2, 3, 3)
    action.click()
    action.perform()


    time.sleep(30)
    # 防止自动退出
    input()
    driver.close()
