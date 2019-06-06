#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/6 0006 21:33 
# @Author : 蓝天下的风 
# @Site :  
# @File : test_login.py 
# @Software: PyCharm


import unittest
from selenium import webdriver
from demo.项目实战框架.PO_V1.PageObjects.login_page import LoginPage
from demo.项目实战框架.PO_V1.PageObjects.index_page import IndexPage
"""
    登录测试用例
    用例三部曲：前置、步骤、断言
"""
class TestLogin(unittest.TestCase):

    def setUp(self):

        #前置 - 打开网页，启动浏览器
        self.driver = webdriver.Chrome()
        self.driver.get("http://120.78.128.25:8765/index/login.html")

    def tearDown(self):
        self.driver.quit()

    # 正常登录
    def test_login_success(self):
        # 步骤 - 登录操作 -登录页面 18684720553   python
        LoginPage(self.driver).login("18684720553","python")
        # 断言 - 页面是否存在  我的账户   元素
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists())
        # URL跳转
        self.assertEqual(self.driver.current_url,"http://120.78.128.25:8765/index/index.html")


        pass

    # 登录失败 异常用例-无密码
    def test_login_failed_by_no_password(self):
        # 步骤 - 登录操作 - 登录页面 -密码为空   17729303803

        # 断言

        pass
