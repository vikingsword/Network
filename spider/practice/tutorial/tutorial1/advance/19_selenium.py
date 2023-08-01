'''
selenium 基本使用：

问题：selenium 模块和爬虫之间的关联：
    - 便捷获取网站中动态加载的数据
    - 便捷实现模拟登陆

selenium使用流程：
    - 环境安装：pip install selenium — 下载一个浏览器的驱动程序(谷歌浏览器)
    一下载路径：http://chromedriver.storage.googleapis.com/index.html
        -驱动程序和浏览器的映射关系：http://blog.csdn.net/huilan_same/article/det
    — 实例化一个浏览器对象
    —编写基于浏览器自动化的操作代码
        -发起请求：get(url)
        — 标签定位：find系列的方法-标签交互：sen_keys('xxx')
        - 执行js程序：excute_script('jsCode')
        - 前进，后退：back()，forward()
        —关闭浏览器：quit()

    -selenium处理iframe
    - 如果定位的标签存在于iframe标签之中，则必须使用switch＿to.frame(id)
    - 动作链(拖动)：from selenium.webdriver import ActionChains
        -实例化一个动作链对象：action＝ActionChains(bro)
        - click＿and＿hold (div)：长按且点击操作
        - move_by_offset(x,y)
        — perform()让动作链立即执行
        - action.release()释放动作链对象
'''

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='./chromedriver.exe')
bro = webdriver.Chrome(service=s)

bro.get('https://www.baidu.com')
time.sleep(2)
input('防止闪退')
bro.quit()
