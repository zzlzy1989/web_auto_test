#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_login
# Author: 简
# Time: 2019/6/6

import unittest
from selenium import webdriver
import ddt

from Demo.PO_V5.PageObjects.login_page import LoginPage
from Demo.PO_V5.PageObjects.index_page import IndexPage
from Demo.PO_V5.TestDatas import login_datas as ld
from Demo.PO_V5.TestDatas import Comm_Datas as cd

import pytest


# 用例三步曲：前置 、步骤 、 断言
# @ddt.ddt
@pytest.mark.login   # 整个TestLogin类里面，所有测试用例都有login标签。
class TestLogin:

    # @classmethod
    # def setUpClass(cls):
    #     # 前置 - 打开网页。启动浏览器
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get(cd.web_login_url)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #
    # def tearDown(self):
    #     # 刷新当前页面
    #     self.driver.refresh()


    # 正常用例 - 登陆+首页
    @pytest.mark.smoke
    def test_login_2_success(self):
        # logging.info("用例1-正常场景-登陆成功-使用到测试数据-")
        # 步骤 - 登陆操作 - 登陆页面 - 18684720553、python
        LoginPage(self.driver).login(ld.success_data["user"],ld.success_data["passwd"])  # 测试对象+测试数据
        # 断言 - 页面是否存在   我的帐户   元素   元素定位+元素操作
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists()) # 测试对象+测试数据
        # url跳转
        self.assertEqual(self.driver.current_url,ld.success_data["check"]) # 测试对象+测试数据 # # 正常用例 - 登陆+首页



    # # 异常用例 -....
    # @ddt.data(*ld.wrong_datas)
    # def test_login_0_failed_by_wrong_datas(self,data):
    #     # 步骤 - 登陆操作 - 登陆页面 - 密码为空 18684720553
    #     LoginPage(self.driver).login(data["user"], data["passwd"])
    #     # 断言 - 页面的提示内容为：请输入密码
    #     self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_loginForm())
    #
    # @ddt.data(*ld.fail_datas)
    # def test_login_1_failed_by_fail_datas(self,data):
    #     # 步骤 - 登陆操作 - 登陆页面 - 密码为空 18684720553
    #     LoginPage(self.driver).login(data["user"], data["passwd"])
    #     # 断言 - 页面的提示内容为：请输入密码
    #     self.assertEqual(data["check"], LoginPage(self.driver).get_error_msg_from_pageCenter())




    # def test_login_failed_by_no_user(self):
    #     # 步骤 - 登陆操作 - 登陆页面 - 用户名为空 python
    #     LoginPage(self.driver).login("", "python")
    #     self.assertEqual("请输入手机号码", LoginPage(self.driver).get_error_msg_from_loginForm())
    #
    # def test_login_failed_by_wrong_user_formater(self):
    #     # 步骤 - 登陆操作 - 登陆页面 - 用户名为空 python
    #     LoginPage(self.driver).login("1867744", "python")
    #     self.assertEqual("请输入正确的手机号", LoginPage(self.driver).get_error_msg_from_loginForm())



