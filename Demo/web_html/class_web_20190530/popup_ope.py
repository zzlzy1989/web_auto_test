#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: popup_ope
# Author: 简
# Time: 2019/5/30

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 2种弹出框
# 1、web页面 - html页面元素 DOM  F12  等到弹出框出现，操作里面元素。

# 2、alert弹框  -- 不是html元素。
   # 切换 - 不是html
   # 接收or no

driver.get("file:///D:/Pychram-Workspace/python15/class_web_20190530/lesson1.html")

# 1、导致alert弹框出现
ele = driver.find_element_by_id("press")
ele.click()  # 导致alert弹框出现

# 2、等待
WebDriverWait(driver,20,0.1).until(EC.alert_is_present())

# 3、切换
alert = driver.switch_to.alert

# 4、使弹出框消失
# print(alert.text)
alert.accept()
# alert.dismiss()
# alert.send_keys()

# 进行后续的其它元素操作。

# selenium当中的元素，有四个基本的操作。
# 1、click()
# 2、send_keys()
# 3、WebElement对象.text  # 文本
# 4、WebElement对象.get_attribute(属性名称)  # 属性获取
