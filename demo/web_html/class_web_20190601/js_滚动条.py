#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/6/7 0007 12:30
# @Author : 蓝天下的风
# @Site :
# @File : study_弹框_popip_up.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 可见/视区域   -  为什么要滚动到可见区域？进行操作。

# 大部分系统在元素操作时，如果元素不在可见区域，随着操作会自动到可见区域 。

#
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

from selenium.webdriver.common.keys import Keys
# 组合键的输入  Keys类
driver.find_element_by_id("kw").send_keys("柠檬班",Keys.ENTER)

locator = (By.XPATH,'//a[contains(text(),"全部课程_在线 培训 视频 教程_腾讯课堂")]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
# 要滚动的元素
ele = driver.find_element_by_xpath('//a[contains(text(),"全部课程_在线 培训 视频 教程_腾讯课堂")]')

# driver和windows是完全不相干的东西。你做你的事情，我做我的事情。按顺序来。
# 假设点了一个元素，导致windows上传窗口出现。
import time
time.sleep(2)
# upload("D:\\111.png")

time.sleep(1)
# 等待要操作元素可见。
driver.find_element_by_xpath("").click()

# 执行js语句
# arguments[0].scrollIntoView();  - 页面顶端
# driver.execute_script("arguments[0].scrollIntoView();",ele)

# arguments[0].scrollIntoView(false);   页面底端
# driver.execute_script("arguments[0].scrollIntoView(false);",ele)

# scrollIntoViewIfNeeded ??? 留做作业。

"""
3、移动到页面底部：
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

4、移动到页面顶部：
     driver.execute_script("window.scrollTo(document.body.scrollHeight,
     0)")
"""
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")







