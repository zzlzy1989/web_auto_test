#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_login_pytest
# Author: 简
# Time: 2019/6/20

from Demo.PO_V6.PageObjects.login_page import LoginPage
from Demo.PO_V6.PageObjects.index_page import IndexPage
from Demo.PO_V6.TestDatas import login_datas as ld
from Demo.PO_V6.TestDatas import Comm_Datas as cd

import pytest

# pytestmark = pytest.mark.model  # 模块级别的标签名


@pytest.mark.demo
@pytest.mark.usefixtures("session_action")
def test_demo():
    print("111111111111111")

@pytest.mark.parametrize("a,b,c",[(1,3,4),(10,35,45),(22.22,22.22,44.44)])
def test_add(a,b,c):
    res = a + b
    assert res == c



# 用例三步曲：前置 、步骤 、 断言
# @ddt.ddt
# @pytest.mark.login   # 整个TestLogin类里面，所有测试用例都有login标签。

@pytest.mark.usefixtures("open_url")  # 使用函数名称为open_url的fixture
@pytest.mark.usefixtures("refresh_page")
class TestLogin:

    pytestmark=pytest.mark.login  # 整个TestLogin类里面，所有测试用例都有

    # 异常用例 -....
    @pytest.mark.parametrize("data", ld.wrong_datas)
    def test_login_0_failed_by_wrong_datas(self, data):
        # 步骤 - 登陆操作 - 登陆页面 - 密码为空 18684720553
        LoginPage(self.driver).login(data["user"], data["passwd"])
        # 断言 - 页面的提示内容为：请输入密码
        self.assertEqual(data["check"], LoginPage(self.driver).get_error_msg_from_loginForm())


    # 正常用例 - 登陆+首页
    @pytest.mark.smoke
    def test_login_2_success(self,open_url): # open_url = driver
        # logging.info("用例1-正常场景-登陆成功-使用到测试数据-")
        # 步骤 - 登陆操作 - 登陆页面 - 18684720553、python
        LoginPage(open_url).login(ld.success_data["user"],ld.success_data["passwd"])  # 测试对象+测试数据
        # 断言 - 页面是否存在   我的帐户   元素   元素定位+元素操作
        assert IndexPage(open_url).check_nick_name_exists() == True  # 测试对象+测试数据
        # url跳转
        assert open_url.current_url == ld.success_data["check"] # 测试对象+测试数据 # # 正常用例 - 登陆+首页



class TestTT:

    pytestmark = pytest.mark.demo
    # pytestmark = [pytest.mark.demo,pytest.mark.demo2]

    def test_add(self):
        c = 100 +200
        assert c == 300

    def test_demo(self):
        print("demo!!!")