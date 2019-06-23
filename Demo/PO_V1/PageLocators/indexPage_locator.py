#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/6/11 0011 21:29
# @Author : 蓝天下的风
# @Software: PyCharm

from selenium.webdriver.common.by import By

class IndexPageLocator:
    # 关于我们
    about_us = (By.XPATH,'//a[text()="关于我们"]')
    # 用户昵称
    user_link = (By.XPATH,'//a[@href="/Member/index.html"]')
    #抢投标按钮
    bid_button = (By.XPATH,'//a[@class="btn btn-special"]')