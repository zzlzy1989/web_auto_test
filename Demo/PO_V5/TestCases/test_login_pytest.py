#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_login_pytest
# Author: 简
# Time: 2019/6/20

from Demo.PO_V5.PageObjects.login_page import LoginPage
from Demo.PO_V5.PageObjects.index_page import IndexPage
from Demo.PO_V5.TestDatas import login_datas as ld
from Demo.PO_V5.TestDatas import Comm_Datas as cd

import pytest


# 用例三步曲：前置 、步骤 、 断言
# @ddt.ddt
@pytest.mark.login   # 整个TestLogin类里面，所有测试用例都有login标签。
@pytest.mark.usefixtures("open_url")  # 使用函数名称为open_url的fixture
class TestLogin:


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

