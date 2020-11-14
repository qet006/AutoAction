import os
# 方便延时加载
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 模拟浏览器打开网站
print("准备打开网页----")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
#window电脑本地
#browser = webdriver.Chrome("D:\Google Chrome\chromedriver.exe")



def scut():
    browser.get('http://fizzcloud.cf/auth/login')
    # 将窗口最大化
    browser.maximize_window()
    print("打开网页了!")
    time.sleep(10)
    # 窗口最大化
    browser.maximize_window()

    # 延迟2秒，用于加载完整
    time.sleep(2)


    # 找到登录表单,发送用户名和密码
    email = "qet006@qq.com"#你的邮箱账户
    password = "124124124"#你的密码
    browser.find_element_by_xpath("/html/body/main/div/div/div/section/div[1]/div/div/div/div/div[2]/form/div[1]/div/div/input").send_keys(email)
    browser.find_element_by_xpath("/html/body/main/div/div/div/section/div[1]/div/div/div/div/div[2]/form/div[2]/div/div/input").send_keys(password)

    # 点击提交按钮
    browser.find_element_by_xpath("/html/body/main/div/div/div/section/div[1]/div/div/div/div/div[2]/form/div[3]/div/div/button").click()


# 进入用户界面，定位签到按钮
browser.find_element_by_xpath("/html/body/main/div[2]/section/div[2]/div[1]/div[1]/div/div[2]/div/div/div/button").click()
    time.sleep(10)
    try:
        browser.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[3]/button").click()
        print("华工申报成功")
        time.sleep(3)
        #saveFile("华工健康申报签到成功！")
    except NoSuchElementException as e:
        print ("华工签到代码存在异常"+str(e))
        # js = 'document.getElementById("btn").click();'
        # browser.execute_script(js)
        #saveFile("华工签到代码存在异常"+str(e))



if __name__ == '__main__':
    scut()
    # situyun()
    # 脚本运行成功,退出浏览器
    browser.quit()
