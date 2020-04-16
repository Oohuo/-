import json

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.keys import Keys
from requests.cookies import RequestsCookieJar
import jo
import chaojiying

def login():
    #chaojiying = chaojiying.Chaojiying_Client('ooohuo', 'ooohuo', '904509')





    browser = webdriver.Chrome()
    browser.get('http://jwmis.hnucm.edu.cn/home.aspx')
    # 打开chrome

    time.sleep(5)
    browser.switch_to.frame('frm_login')
    # 跳转表单

    browser.find_element_by_id("txt_sdertfgsadscxcadsads").click()
    jpg = browser.find_element_by_id('imgCode')
    img_src = jpg.get_attribute("src")
    print(img_src)
    # 拿到验证码url

    # 在这里应该使用browser的ASP.NET_SessionId的值
    cookie_bro = browser.get_cookies()
    print(cookie_bro)
    # 获取browser的cookie字典
    # print(cookie_bro)

    cookie1 = cookie_bro[2]['value']
    cookie2 = cookie_bro[1]['value']
    print("\n当前cookie为： " + cookie1)

    headers1 = {
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'name=value; name=value; myCookie=; ASP.NET_SessionId=' + cookie1 + '; BINGOCLOUDLB=' + cookie2,
        'Host': 'jwmis.hnucm.edu.cn',
        'Referer': 'http://jwmis.hnucm.edu.cn/_data/login_home.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }

    # proxy1={"http":"http://127.0.0.1:8080"}
    # r=requests.get(img_src,headers=headers1,proxies=proxy1)
    # requests代理

    r = requests.get(img_src, headers=headers1)
    img_content = r.content
    print("\n[*]正在下载验证码...\n")
    with open('check.jpg', 'wb') as f:
        f.write(img_content)

    time.sleep(1)
    # print("[*]验证码下载完成！\n")
    # # text=jo('check.jpg')
    # im = open('check.jpg', 'rb').read()
    # c = chaojiying.PostPic(im, 1004)
    #
    # text = c['pic_str']
    #
    # print("[*]验证码识别为：" + text)
    print("[*]验证码下载完成！\n")
    text = jo.jo('check.jpg')
    print(text)
    t1 = text[3]
    t2 = text[7]
    t3 = text[11]
    t4 = text[-1]
    code = t1 + t2 + t3 + t4
    print("[*]验证码识别为：" + code)

    #把对应的“学号”和“密码”换成自己的
    browser.find_element_by_id("txt_asmcdefsddsd").send_keys("201701090133")
    browser.find_element_by_id("txt_asmcdefsddsd").send_keys(Keys.TAB)
    browser.find_element_by_id("txt_pewerwedsdfsdff").send_keys("990922")
    time.sleep(4)
    #browser.find_element_by_id("txt_sdertfgsadscxcadsads").send_keys(text)
    browser.find_element_by_id("btn_login").click()

    # time.sleep(4)
    # browser.close()
    # 关闭浏览器


if __name__ == '__main__':
    login()