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
import time

driver = webdriver.Chrome()
driver.get("E:\PycharmProjects\web_auto_test\demo\web_html\demo_html\lesson_html.html")
# 1、driver.find_element_by_xpath('//*[@id="js-mod-header-login"]//a[text()="登录"]').click()
driver.find_element_by_id("press").click()
# 2、等待
WebDriverWait(driver,20).until(EC.alert_is_present())

# 3、切换
alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()
# alert.dismiss()
# alert.send_keys()

# 4、进行后续其他元素操作
# selenium 当中的元素，有四个基本的操作
# 1、click()
# 2、send_keys()
# 3、WebElement对象.ele.text # 文本
# 4、WebElement对象.get_attribute(属性名称) # 属性获取

# driver.quit()


# 两种弹出框
# 1、web页面-- html页面元素，DOM 等待弹出框出现，操作里面的元素

# 2、alert方法 不是html页面的元素
# 定位弹出框：selenium如何处理? driver.switch_to.alert
# dismiss取消    accept确认    send_keys输入
# driver.switch_to.alert

