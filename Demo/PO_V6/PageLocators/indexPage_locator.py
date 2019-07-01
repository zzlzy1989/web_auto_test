#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/11/23 20:48
from selenium.webdriver.common.by import By
class IndexPageLocator:
    # 关于我们
    about_us = (By.XPATH,'//a[text()="关于我们"]')
    # 用户昵称
    user_link = (By.XPATH,'//a[@href="/Member/index.html"]')
    #抢投标按钮
    bid_button = (By.XPATH,'//a[@class="btn btn-special"]')