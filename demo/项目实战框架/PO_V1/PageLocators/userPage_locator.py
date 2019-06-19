#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/11/23 21:44
from selenium.webdriver.common.by import By

class UserPageLocator:

    #可用余额
    user_leftMoney = (By.XPATH,'//li[@class="color_sub"]')