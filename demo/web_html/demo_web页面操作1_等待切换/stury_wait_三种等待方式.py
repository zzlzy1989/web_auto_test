#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/29 0029 20:55 
# @Author : 蓝天下的风 
# @Site :  
# @File : 学习等待-三种等待方式.py 
# @Software: PyCharm

from selenium import webdriver

import time

#浏览器会话的开始

driver = webdriver.Chrome()

#设置全局等待时间
driver.implicitly_wait(30)

driver.get("http://www.baidu.com")
driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()


# 1、当你的操作带来了页面的变化，请一定要等待
# time.sleep(5)#傻等


# 2、隐形等待-智能等待：如果你10秒出现了，我就开始下一步操作。设置上限：30秒 超时TimeoutException

# 3、显性等待-智能等待：明确的条件（元素可见，窗口存在）。等待+条件
# （如果你10秒出现了，我就开始下一步操作。）
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 元素存在（html里面，能找到）；
# 元素可见（存在并且可见-看得见大小-可见才可操作）；
# 元素可用（可见之后，才有可用的可能性。只读/不可点击-不可用）


# 等待条件表达
# locater = (定位类型，定位表达式)
locater = (By.ID,'TANGRAM__PSP_10__footerULoginBtn')
# EC.visibility_of_element_located(locater) #条件
# 等待元素可见
WebDriverWait(driver,30).until(EC.visibility_of_element_located(locater))
# 使用sleep短暂等待，辅助- 0.5秒
time.sleep(0.5)
# 点击元素
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()


#关闭当前窗口
driver.close()
#浏览器会话结束  关闭浏览器关闭了chromedriver
driver.quit()