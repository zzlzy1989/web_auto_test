#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: conftest
# Author: 简
# Time: 2019/6/20

# fixture = 前置+后置

# 如果很多用例都有同样的前置和后置，那么我就只实现一个，然后需要的用例就去调用就好了。

# 机制：与测试用例同级，或者是测试用例的父级，创建一个conftest.py文件。
# conftest.py文件里：放所有的前置和后置。 不需要用例.py文件主动引入conftest文件。

# 模板层级：子层级可以有自己的conftest.py文件。用例优先使用自己层级的conftest。

# 怎么定义fixture?
# 定一个函数：包含前置操作+后置操作。
# 把函数声明为fixture :在函数前面加上 @pytest.fixture(作用级别=默认为function)

# 不能够与unittest兼容。

from selenium import webdriver
import pytest

from Demo.PO_V6.TestDatas import Comm_Datas as cd


# 全局变量
driver = None

# fixture的定义。如果有返回值，那么写在yield后面。
# 在测试用例当中，调用有返回值的fixture函数时，函数名称就是代表返回值。
# 在测试用例当中，函数名称作为用例的参数即可。
@pytest.fixture(scope="class")  #
def open_url():
    global driver
    # 前置
    driver = webdriver.Chrome()
    driver.get(cd.web_login_url)
    yield driver  # yield之前代码是前置，之后的代码就是后置。
    # 后置
    driver.quit()


# 刷新页面 - 定义的第二个fixture
@pytest.fixture
def refresh_page():
    yield
    global driver
    driver.refresh()


# session级别的
@pytest.fixture(scope="session")
def session_action():
    print("===== 会话开始，测试用例开始执行=====")
    yield
    print("===== 会话结束，测试用例全部执行完成！=====")



# 在测试用例中使用fixture
# @pytest.mark.usefixtures("函数名称")

@pytest.fixture(scope="class")
def login_web():
    pass