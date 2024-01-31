import time
from selenium import webdriver
# 动作链
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='../chromedriver.exe')
bro = webdriver.Chrome(service=s)

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
bro.get(url)
# 如果定位的标签是在iframe标签中的，则必须通过如下操作进行标签定位
# 切换浏览器标签的作用域
bro.switch_to.frame('iframeResult')
div = bro.find_element(By.ID, value='draggable')

action = ActionChains(bro)
# 点击长按指定标签
action.click_and_hold(div)
for i in range(5):
    # perform 立即执行动作链
    action.move_by_offset(50, 0).perform()
    # action.drag_and_drop_by_offset(div, 50, 0).perform()
    time.sleep(0.5)
action.release().perform()

print(div)

time.sleep(3)
bro.quit()
