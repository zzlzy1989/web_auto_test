#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time     : 2019/6/20 0020 21:46 
# @Author   : 蓝天下的风  
# @File     : test_login_pytest.py 
# Project   : web_auto_test
# @Software : PyCharm


import pytest
from Demo.项目实战框架.PO_V1.PageObjects.login_page import LoginPage
from Demo.项目实战框架.PO_V1.PageObjects.index_page import IndexPage
from Demo.项目实战框架.PO_V1.TestDatas import login_datas as ld



@pytest.mark.login
@pytest.mark.usefixtures("open_url")   #使用函数名称为open_url的fixture
class TestLogin:

    # 正常登录
    def test_login_2_success(self,open_url):
        # 步骤 - 登录操作 -登录页面 18684720553   python
        LoginPage(open_url).login(ld.success_data["user"],ld.success_data["passwd"])
        # 断言 - 页面是否存在  我的账户   元素
        assert IndexPage(open_url).check_nick_name_exists()
        # URL跳转
        assert open_url.current_url == ld.success_data["check"]
