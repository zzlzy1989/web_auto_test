#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/11 0011 21:29 
# @Author : 蓝天下的风 
# @Site :  
# @File : login_page_locater.py 
# @Software: PyCharm

from selenium.webdriver.common.by import By

# 存放登录的 元素定位
class LoginPageLocator:

    # 用户名输入框
    user_loc = (By.XPATH,'//input[@name="phone"]')
    # 密码输入框
    passwd_loc = (By.XPATH,'// input[ @ name = "password"]')
    # 登录按钮
    login_button_loc = (By.XPATH,'//button')
    # 提示框 - 登录表单区域
    error_notify_from_loginForm = (By.XPATH,'//div[@class="form-error-info"]')
    # 提示框 - 中间区域
    error_notify_from_pageCenter = (By.XPATH,'//div[@class="layui-layer-content"]')