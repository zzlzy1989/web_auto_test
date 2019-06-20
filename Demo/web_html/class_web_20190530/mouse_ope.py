#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: mouse_ope
# Author: 简
# Time: 2019/5/30
# 实例化ActionChains()

# 鼠标操作类 ActionChains   链式操作
# 悬浮 - 最多 move_to_element
# 右键   context_click
# 点击   click
# 双击   double_click
# 拖拽   drag_and_drop
# 滚动 --- js
# 按住左键不松   click_and_hold
# 释放  release

# 重置 reset_actions
# 执行操作 perform() # 一定要带

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# 先找到设置
ele = driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_settingicon"]')

# # 1、实例化
# ac = ActionChains(driver)
#
# # 2、鼠标操作
# ac.move_to_element(ele) # 悬浮
# ac.click(ele)   # 点击
#
# # 3、执行动作
# # ac.perform()

import time
# 设置选项出来
ActionChains(driver).move_to_element(ele).click(ele).perform()

# 选择下拉列表当中的值。
# //a[text()="高级搜索"]
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]')))
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()


# Select类来处理select/option元素
# 可以通过value，index,text三种方式选择option对应的值。

# 1、找到select元素对象，实例化Select类。
s = Select(driver.find_element_by_xpath('//select[@name="ft"]'))

# 2、选择下拉列表的值。
# 2.1 value属性值
time.sleep(2)
s.select_by_value("ppt")

time.sleep(2)
s.select_by_index(1)  # 从0开始

time.sleep(2)
s.select_by_visible_text("所有格式")


# iframe和alert弹出框  - driver.switch_to.frame()/alert-Alert类
# 鼠标操作 - ActionChains类
# 下拉列表 - Select类

# key，js，上传文件