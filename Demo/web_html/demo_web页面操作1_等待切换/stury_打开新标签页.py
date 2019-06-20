#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/29 0029 22:36 
# @Author : 蓝天下的风 
# @Site :  
# @File : 学习打开新标签页.py 
# @Software: PyCharm

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#浏览器会话的开始

driver = webdriver.Chrome()

#设置全局等待时间
driver.implicitly_wait(30)

driver.get("http://www.baidu.com")

# 输入柠檬班并点击百度一下
# driver.find_element_by_id('kw').clear() #清除文本
driver.find_element_by_id('kw').send_keys('柠檬班')
driver.find_element_by_id("su").click()
# 等待 //a[text()="_腾讯课堂"]
locator = (By.XPATH,'//a[text()="_腾讯课堂"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))

# ------------------------------------------------------------
# 点击柠檬班_腾讯课堂
# driver.find_element_by_xpath('//a[text()="_腾讯课堂"]').click()
# 方式二
# step1:获取窗口数
handles = driver.window_handles # >>> 只有一个 窗口
# step2:打开新窗口的操作
driver.find_element(*locator).click()   #本操作带来新窗口的出现  >>> 2个窗口

############ 第二种 ###########
# step3:确认新窗口出现了，我再去操作他，等待新窗口出现
# EC.new_window_is_opened # 比窗口总数的大小  # 传一个窗口的总数
WebDriverWait(driver,10).until(EC.new_window_is_opened(handles))   #2>1 确认新窗口出现
# step4:再次获取 窗口的handles
handles = driver.window_handles
# step5:切换 新的窗口
driver.switch_to.window(handles[-1])
# ------------------------------------------------------------

# ------------------------------------------------------------
driver.find_element(*locator).click()   #本操作带来新窗口的出现
######## 第一种 ##########
# 打开新的窗口
#   1、获取所有的窗口
handles = driver.window_handles
print(driver.window_handles)
#   当前窗口的handle
print(driver.current_window_handle)
#   2、切换新的窗口
driver.switch_to.window(handles[-1])
print("切换之后的窗口为：",driver.current_window_handle)
# ------------------------------------------------------------

# 新的窗口当中，点击 课程
# 等待
locator = (By.XPATH,'//section[@class="section-main"]//h2[contains(text(),"课程")]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
driver.find_element(*locator).click()

