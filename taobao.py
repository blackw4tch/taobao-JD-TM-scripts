from selenium import webdriver
import datetime
import time


def login():
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("请在20秒内完成扫码")
        time.sleep(20)
        browser.get("https://cart.taobao.com/cart.htm")
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
                    if browser.find_element_by_link_text("结 算"):
                        browser.find_element_by_link_text("结 算").click()
                        print("结算成功")
                        break
                except:
                    pass
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
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
    browser = webdriver.Chrome()
    browser.maximize_window()
    login()
    buy(times)