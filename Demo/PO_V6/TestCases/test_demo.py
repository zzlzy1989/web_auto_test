#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time     : 2019/6/24 0024 21:14 
# @Author   : 蓝天下的风  
# @File     : test_demo.py 
# Project   : web_auto_test
# @Software : PyCharm

'''

'''
import pytest

@pytest.fixture
def myfix_1():
    print("\n----------开始 第一个myfix 1")
    a = True
    yield a
    print("----------结束 第一个myfix 1")


@pytest.fixture
def myfix_2_bigger(myfix_1):

    print("=========开始 第二个myfix_2_bigger======")
    print(myfix_1)
    c = None
    if myfix_1==True:
        c="YES"
    else:
        c="NO"
    yield
    print("=========结束 第二个myfix_2_bigger======")



def test_demo(myfix_2_bigger): # fixtures的函数名称作为用例参数，同时也是接收返回值
    print("--------------------测试用例---------------------")