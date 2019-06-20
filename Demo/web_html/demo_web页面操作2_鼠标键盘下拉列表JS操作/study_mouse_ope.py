#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/7 0007 13:46 
# @Author : 蓝天下的风 
# @Site :  
# @File : study_mouse_ope.py 
# @Software: PyCharm

# 鼠标操作类 ActionChains 链式操作
# 悬浮    move_by_offset
# 右键    context_click
# 点击    click
# 拖拽    drag_and_drop
# 双击    double_click
# 滚动    ---js
# 按住左键不松    click_and_hold
# 执行操作 perform()

# 重置 reset_actions
# 执行操作 perform() # 必须步骤

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 先找到设置
ele = driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_settingicon"]')

# # 1、实例化
# ac = ActionChains(driver)
# # 2、鼠标操作
# ac.move_to_element(ele) # 悬浮
# ac.click()
# # 3、执行操作
# ac.perform()

# 链式操作
ActionChains(driver).move_to_element(ele).click(ele).perform()

# 等待
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]')))
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()

# Select 类来处理select / option元素
# 可以通过value,index,text三种方式选择option对应的值

# 1、找到select 元素对象，实例化select 类.
s = Select(driver.find_element_by_xpath('//select[@name="ft"]'))

# 2、选择下来列表的值
# 2.1 value属性值time.sleep(2)
# s.select_by_value("doc")
#
# time.sleep(2)
# s.select_by_index(1)
#
# time.sleep(2)
# s.select_by_visible_text("所有格式")


#总结：
# iframe 和 alert弹出框
# 鼠标操作 ActionChains类
# 下拉列表 -- Select类 3种方式 select_by_value、select_by_index、select_by_visible_text

#