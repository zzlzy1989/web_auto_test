#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/6 0006 20:59 
# @Author : 蓝天下的风 
# @Site :  
# @File : login_page.py 
# @Software: PyCharm

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from demo.项目实战框架.PO_V1.PageLocators.login_page_locator import LoginPageLocator as loc
# 一个用例，一次浏览器的打开和结束
class LoginPage:

    # 属性
    def __init__(self,driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()
        # self.driver.get("http://120.78.128.25:8765/index/login.html")

    # 登录功能
    def login(self,username,password):
        #等待
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located)
        # 输入用户名、输入密码、点击登录
        self.driver.find_element(*loc.user_loc).send_keys(username)
        self.driver.find_element(*loc.passwd_loc).send_keys(password)
        self.driver.find_element(*loc.login_button_loc).click()

    # 获取表单区域的错误文本信息
    def get_error_msg_from_loginForm(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(*loc.error_notify_from_loginForm))
        return self.driver.find_element(*loc.error_notify_from_loginForm).text

    # 获取页面中间的错误文本信息
    def get_error_msg_from_pageCenter(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(*loc.error_notify_from_pageCenter))
        return self.driver.find_element(*loc.error_notify_from_pageCenter).text





# if __name__ == '__main__':
#     loginPage = LoginPage()
#     loginPage.login("17792303803","python")





