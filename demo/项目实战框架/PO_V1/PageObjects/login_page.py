#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/6 0006 20:59 
# @Author : 蓝天下的风 
# @Site :  
# @File : login_page.py 
# @Software: PyCharm

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from demo.项目实战框架.PO_V1.PageLocators.login_page_locator import LoginPageLocator as loc
from demo.项目实战框架.PO_V1.Common.basepage import BasePage
# 一个用例，一次浏览器的打开和结束
class LoginPage(BasePage):

    # 登陆功能
    def login(self,user,passwd):
        self.input_text(loc.user_loc,user,"登陆页面_输入用户名")
        self.input_text(loc.passwd_loc,passwd,"登陆页面_输入密码")
        self.click_element(loc.login_button_loc,"登陆页面_点击登陆按钮")

    # //div[@class="form-error-info"]
    # 获取表单区域的错误信息
    def get_error_msg_from_loginForm(self):
        self.wait_eleVisible(loc.error_notify_from_loginForm,"登陆页面_表单区域错误信息")
        return self.get_element_text(loc.error_notify_from_loginForm,"登陆页面_表单区域错误信息")

    # 获取页面中间的错误信息
    def get_error_msg_from_pageCenter(self):
        self.wait_eleVisible(loc.error_notify_from_pageCenter,"登陆页面_页面中间错误信息")
        return self.get_element_text(loc.error_notify_from_pageCenter,"登陆页面_页面中间错误信息")






# if __name__ == '__main__':
#     loginPage = LoginPage()
#     loginPage.login("17792303803","python")





