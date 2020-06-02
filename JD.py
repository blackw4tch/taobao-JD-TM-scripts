from selenium import webdriver
from pykeyboard import PyKeyboard
import datetime
import time


def login():
    browser.get("https://www.jd.com/")
    time.sleep(3)
    if browser.find_element_by_link_text("你好，请登录"):
        browser.find_element_by_link_text("你好，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        browser.get("https://cart.jd.com/cart.action")
    time.sleep(3)

    now = datetime.datetime.now()
    print('登陆成功:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(times):
    print("请手动勾选需要购买的商品")
    break2 = 2
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > times:
            while True:
                try:
                    if browser.find_element_by_link_text("去结算"):
                        browser.find_element_by_link_text("去结算").click()
                        print("结算成功")
                        break
                except:
                    pass
            while True:
                try:
                    try:
                        if browser.find_element_by_xpath('//*[@id="quark-pw-list"]/i[1]'):
                            browser.find_element_by_xpath('//*[@id="quark-pw-list"]/i[1]').click()
                            k.tap_key('1')
                            k.tap_key('9')
                            k.tap_key('6')
                            k.tap_key('4')
                            k.tap_key('0')
                            k.tap_key('0')
                    except:
                        browser.find_element_by_xpath('//*[@id="order-submit"]')
                        browser.find_element_by_xpath('//*[@id="order-submit"]').click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("抢购成功时间：%s" % now1)
                        break2 = 1
                        break
                except:
                    print("再次尝试提交订单")
                    time.sleep(0.01)
        if break2 == 1:
            break
        time.sleep(0.01)

if __name__ == "__main__":
    times = input("请输入抢购时间，格式如(2020-06-01 11:20:00.000000):")
    k = PyKeyboard()
    browser = webdriver.Chrome()
    browser.maximize_window()
    login()
    buy(times)