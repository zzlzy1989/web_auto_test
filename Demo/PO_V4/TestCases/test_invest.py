#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_invest
# Author: 简
# Time: 2019/6/13


"""
用例1：正常投资，投资金额：1000
异常用例:
  1）投资为10   提示  要为100的整数倍
  2）投资为12   提示   要为10的整数倍
  3）投资为非数字  提示  要为1-的整数倍
  4）投资为0/负数/含空格/空   提示   请正确填写投标金额

  # 5）投资数 > 标总可投额  提示   购买标的金额不能大于标剩余金额
  #    # 充值10万，创建一个借款9万块的标
  #
  # 6）投资数 > 你可用余额 且 标可投 > 投资数  提示   你投的钱 > 你能投的钱
  #   你只有10万，你要投20万，标的可投为200万
  #   # 另外一个帐号，永远都是10万。创建一个标为200万   你去投20万
"""
# 前置(准备工作-)、步骤(用户页面操作)、断言(页面操作)
# 前置 - 通过代码来创建前置 - 尽量少的依赖环境数据
"""
1、投资帐号登陆；
2、要有可投的标 - 有可投余额。没有就加标？--- 接口
3、用户余额充足 - 充值5000块线 - 接口实现
               - 钱 > 投资金额  - 不充。不大了呢，一口气充2000000
               - 充个2000万 ()
                
"""
# 步骤
"""
1、首页 - 选一个标，进入标页面
2、投资页面 - 输入金额，进行投资
"""
# 断言
"""
1、个人页面 - 个人余额少的部分 == 投资前的金额 - 投资后的金额
2、投资记录
3、标的可投金额  - 投资金额 = 投资之后的金额 
"""

import unittest
import logging
from selenium import webdriver
from Demo.PO_V4.Common import logger
import time
import ddt

from Demo.PO_V4.TestDatas import Comm_Datas as CD
from Demo.PO_V4.TestDatas import invest_datas as ID

from Demo.PO_V4.PageObjects.login_page import LoginPage
from Demo.PO_V4.PageObjects.bid_page import BidPage
from Demo.PO_V4.PageObjects.index_page import IndexPage
from Demo.PO_V4.PageObjects.user_page import UserPage

@ddt.ddt
class TestInvest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 初始化浏览器会话
        logging.info("=====用例类前置：初始化浏览器会话，登陆前程贷系统=======")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(CD.web_login_url)
        LoginPage(cls.driver).login(CD.user, CD.passwd)
        # 首页 - 选一个标来投资 - 直接选第一个标 - --- / 随机选一个
        IndexPage(cls.driver).click_invest_button()
        cls.bid_page = BidPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        logging.info("=====用例类后置：关闭浏览器会话,清理环境=======")
        cls.driver.quit()

    def tearDown(self):
        logging.info("=====每一个用例后置：刷新当前页面=======")
        self.driver.refresh()
        time.sleep(0.5)

    def test_invest_1_success(self):
        logging.info("*********投资用例：正常场景-投资成功*********")
        # 标页面 - 获取投资前的个人余额
        userMoney_beforeInvest = self.bid_page.get_user_money()
        # 标页面 - 输入投资金额 ，点击投标按钮
        self.bid_page.invest(ID.success["money"])
        # 标页面 - 投资成功弹出框 ，点击查看并激活按钮
        self.bid_page.click_activeButton_on_success_popup()
        # #验证
        # 个人页面 - 获取用户当前余额
        userMoney_afterInvest = UserPage(self.driver).get_user_leftMoney()
        # 1、余额：投资前获取一下，投资后再获取一下。求差值，如果等于投资金额，那正确。
        assert ID.success["money"] == int(float(userMoney_beforeInvest) - float(userMoney_afterInvest))
        # PS：自动化测试独立帐号。
        # 2、个人页面 - 投资记录获取。

    @ddt.data(*ID.wrong_format_money)
    def test_invest_0_failed_by_No100(self, data):
        logging.info("*********投资用例：异常场景：投资金额为非100的整数倍、错误的格式等*********")
        # 标页面 - 获取投资前的个人余额
        userMoney_beforeInvest = self.bid_page.get_user_money()
        # 标页面 - 输入投资金额 ，点击投标按钮
        self.bid_page.invest(data["money"])
        # 获取提示信息
        errorMsg = self.bid_page.get_errorMsg_from_pageCenter()
        # 刷新
        self.driver.refresh()
        # 获取用户余额
        userMoney_afterInvest = self.bid_page.get_user_money()
        # 断言
        assert errorMsg == data["check"]
        assert userMoney_afterInvest == userMoney_beforeInvest




    # def test_invest_success(self):
    #     # 2000 步骤
    #     # 首页 - 选标投资
    #     # 获取 个人余额、获取 当前标的可投金额
    #     # 标页面 - 获取用户余额、获取标的可投金额
    #     # 标页面 - 投资操作 2000
    #     # 标页面 - 弹出框
    #     # 断言
    #     # 投资金额  = 投资前的钱 - 投资后的钱
    #     # 个人页面 - 获取投资后的用户可用余额
    #     # 标页面 - 获取投资后的标可投金额
    #     pass
    #
    # def test_invest_failed_wrong_format(self):
    #     # 首页 - 选标投资
    #     # 获取 个人余额、获取 当前标的可投金额
    #     # 标页面 - 获取用户余额、获取标的可投金额
    #     # 标页面 - 投资操作 10/-1/0/$%%%/空
    #     # 断言
    #     # 提示信息对不对？？
    #     # 个人的钱有没有少？？
    #     pass
