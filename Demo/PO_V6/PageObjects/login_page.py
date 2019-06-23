#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: login_page
# Author: 简
# Time: 2019/6/6



from Demo.PO_V6.PageLocators.login_page_locator import LoginPageLocator as loc
from Demo.PO_V6.Common.basepage import BasePage
# 一个用例，一次浏览器的打开和结束。
class LoginPage(BasePage):


    # 登陆功能
    def login(self,user,passwd):
        self.input_text(loc.user_loc,"登陆页面_输入用户名",user)
        self.input_text(loc.passwd_loc,"登陆页面_输入密码",passwd)
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

