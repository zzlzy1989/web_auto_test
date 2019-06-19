#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/6/7 0007 12:30
# @Author : 蓝天下的风
# @Site :
# @File : study_弹框_popip_up.py
# @Software: PyCharm
# send_keys()

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

from selenium.webdriver.common.keys import Keys
# 组合键的输入  Keys类
driver.find_element_by_id("kw").send_keys("柠檬班",Keys.ENTER)