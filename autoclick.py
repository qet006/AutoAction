# -*- coding: utf-8 -*-
import os
# 方便延时加载
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#import requests

QLog =""
# 模拟浏览器打开网站
print("准备打开网页----")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# git打开
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
# window电脑本地
#browser = webdriver.Chrome(executable_path='D:\ChromePortable\App\Google Chrome\chromedriver')

#****************************portableappk签到***开始
def qiaodao():
    browser.get(
        "https://portableappk.com/point-manage/")
    log_print("打开网站了!")
#     # 获取当前页面title并断言
#     title = browser.title
#     print("当前页面的title是：", title, "\n")
#     # 获取当前页面url并断言
#     currentPageUrl = browser.current_url
#     print("当前页面的url是：", currentPageUrl)
    time.sleep(5)
    t = browser.find_element_by_css_selector('.widget-my-cred')
    log_print("用户中心："+ t.text)
    if t.text.find('用户等级') == -1:
        browser.find_element_by_css_selector('.widget-my-cred a:nth-child(1)').click()
        if browser.current_url.find('wp-login.php')>-1:
            qd()
        else:
            log_print("***错误!!未到登录页面***")
            return 
    logoin()

def logoin():
    if browser.current_url.find('wp-admin')>-1:
        browser.find_element_by_css_selector("#wp-admin-bar-site-name").click()
    time.sleep(5)
    log_print("准备登录******")
    obj=browser.find_element_by_css_selector('#checkin')
    log_print("签到按钮文本:"+obj.text)
    if obj.text=='打卡签到':
        log_print("******开始签到******")
        obj.click()
        time.sleep(10)
        if obj.text=="签到完毕":
            log_print("签到完毕*****"+browser.find_element_by_css_selector('#my-balance span').text)
        else:    
            log_print("******未找效验成功请人工查验******")  
        log_print("******签到完成******")
    else:
        if obj.text=="签到完毕":
            log_print("签到完毕*****"+browser.find_element_by_css_selector('#my-balance span').text)
        else:    
            log_print("******未找到签到按钮******")      
    sendmeg()


def qd():
    dlcs=1
    while browser.current_url.find('wp-login.php')>-1:
        log_print("准备签到"+str(dlcs))
        username = os.environ['SCUT_USER']
        password = os.environ['SCUT_PASSWORD']
        log_print("username: "+username+"  password: "+password)
        time.sleep(1)
        obj=browser.find_element_by_css_selector('#user_login')
        obj.clear()
        obj.send_keys(username)
        browser.find_element_by_css_selector('#user_pass').send_keys(password)
        t1=zh(browser.find_element_by_css_selector('.cptch_span:nth-child(1)').text)
        t2=browser.find_element_by_css_selector('.cptch_span:nth-child(2)').text
        t3=zh(browser.find_element_by_css_selector('.cptch_span:nth-child(3)').text)
        t5=zh(browser.find_element_by_css_selector('.cptch_span:nth-child(5)').text)
        while (t1=='' and t3=='') or (t1=='' and t5=='') or (t3=='' and t5==''):
            browser.find_element_by_css_selector('.cptch_reload_button').click()
            time.sleep(2)
            t1=zh(browser.find_element_by_css_selector('.cptch_span:nth-child(1)').text)
            t2=browser.find_element_by_css_selector('.cptch_span:nth-child(2)').text
            t3=zh(browser.find_element_by_css_selector('.cptch_span:nth-child(3)').text)
            t5=zh(browser.find_element_by_css_selector('.cptch_span:nth-child(5)').text)
        
        browser.find_element_by_css_selector('.cptch_wp_login').send_keys(zhfh(t1,t2,t3,t5))
        browser.find_element_by_css_selector('#wp-submit').click()
        time.sleep(2)
        dlcs=dlcs+1

def zh(s):
    if s=='': return ''
    if s=='0' or s=='零':
        return 0
    if s=='1' or s=='一':
        return 1
    if s=='2' or s=='二':
        return 2
    if s=='3' or s=='三':
        return 3
    if s=='4' or s=='四':
        return 4
    if s=='5' or s=='五':
        return 5
    if s=='6' or s=='六':
        return 6
    if s=='7' or s=='七':
        return 7
    if s=='8' or s=='八':
        return 8
    if s=='9' or s=='九':
        return 9
    if len(s)>1 and s.find('十')<0:
        return int(s)
    return ''    

def zhfh(t1,t2,t3,t5):
    if t2==' + ':
        if t1=='': return str(int(t5-t3))
        if t3=='': return str(int(t5-t1))
        if t5=='': return str(int(t3+t1)) 
    if t2==' − ':
        if t1=='': return str(int(t5+t3))
        if t3=='': return str(int(t1-t5))
        if t5=='': return str(int(t1-t3)) 
    if t2==' × ' :
        if t1=='': return str(int(t5/t3))
        if t3=='': return str(int(t5/t1))
        if t5=='': return str(int(t1*t3)) 
        
       
 #****************************portableappk签到***结束

def log_print(nr):
    global QLog
    print(nr)  
    QLog =QLog +"  <br/>  " +nr

def sendmeg():
    api = "https://sc.ftqq.com/SCU124619T832fb34a7837a9739824a610d986adfb5fa7fbce6b018.send"
    data = {
    "text":"绿色签到",
    "desp":QLog
    }
   # req = requests.post(api,data = data)   

if __name__ == '__main__':
    qiaodao()
    # 脚本运行成功,退出浏览器
    browser.quit()
