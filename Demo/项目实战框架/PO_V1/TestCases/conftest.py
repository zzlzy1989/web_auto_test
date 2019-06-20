#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time     : 2019/6/20 0020 21:31 
# @Author   : 蓝天下的风  
# @File     : conftest.py 
# Project   : web_auto_test
# @Software : PyCharm



from selenium import webdriver
import logging,time
import pytest
from Demo.项目实战框架.PO_V1.TestDatas import Common_Datas as CD


# fixture 的定义，如果有返回值，那么写在yield后面
# 在测是用例当中，
# 在测试用例当中，
@pytest.fixture(scope="class")
def open_url():
    # 前置
    driver= webdriver.Chrome()
    driver.get(CD.web_login_url)

    # yield 之前的代码时前置，之后的代码是后置
    yield driver
    # 后置
    driver.quit()


# 在测试用例中使用 fixture
# @