import time

from selenium import webdriver
from time import sleep
# 导入动作链对应的类
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service

s = Service(executable_path='../advance/chromedriver.exe')
bro = webdriver.Chrome(service=s)
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 如果定位的标签是存在于iframe标签之中的，则必须通过如下操作进行标签定位
bro.switch_to.frame('iframeResult')  # 切换浏览器标签定位的作用域
div = bro.find_element(by='id', value='draggable')

# 动作链
# 实例化动作链
action = ActionChains(bro)
# 点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    # .perform()：立即执行动作链操作
    # x：水平方向；y：竖直方向
    action.move_by_offset(17, 0).perform()
    sleep(0.3)

# 释放动作链
action.release()

time.sleep(2)

bro.quit()
