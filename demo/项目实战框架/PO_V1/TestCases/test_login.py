#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/6 0006 21:33 
# @Author : 蓝天下的风 
# @Site :  
# @File : test_login.py 
# @Software: PyCharm


import unittest
import ddt
from selenium import webdriver

from demo.项目实战框架.PO_V1.PageObjects.login_page import LoginPage
from demo.项目实战框架.PO_V1.PageObjects.index_page import IndexPage
from demo.项目实战框架.PO_V1.TestDatas import login_datas as ld
from demo.项目实战框架.PO_V1.TestDatas import Common_data as cd
"""
    登录测试用例
    用例三部曲：前置、步骤、断言
"""
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        #前置 - 打开网页，启动浏览器
        cls.driver = webdriver.Chrome()
        cls.driver.get(cd.base_url+"/index/login.html")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()

    # 正常登录
    def test_login_2_success(self):
        # 步骤 - 登录操作 -登录页面 18684720553   python
        LoginPage(self.driver).login(ld.success_data["user"],ld.success_data["passwd"])
        # 断言 - 页面是否存在  我的账户   元素
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists())
        # URL跳转
        self.assertEqual(self.driver.current_url,cd.base_url+"/index/index.html")


    @ddt.data(*ld.wrong_datas)
    # 登录失败 异常用例-无密码
    def test_login_0_failed_by_wrong_data(self,data):
        # 步骤 - 登录操作 - 登录页面 -密码为空   17729303803
        LoginPage(self.driver).login(data["user"], data["passwd"])
        # 断言
        self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_loginForm())

    @ddt.data(*ld.fail_datas)
    # 登录失败 用户名或密码不准确
    def test_login_1_failed_by_fail_data(self,data):
        # 步骤 - 登录操作 - 登录页面
        LoginPage(self.driver).login(data["user"], data["passwd"])
        # 断言
        self.assertEqual(data["check"], LoginPage(self.driver).get_error_msg_from_loginForm())

