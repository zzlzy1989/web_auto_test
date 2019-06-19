#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: switch_to_iframe
# Author: 简
# Time: 2019/5/30

from selenium import webdriver

# 3、智能等待：明确的条件(元素可见、窗口存在。。。)。  等待+条件
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# html 里面  再嵌套一个 html
# DOM -- 只针对一个html id，xpath

# 1、如果你要操作的元素，在iframe当中，你才去切换 。F12,

# 2、确认iframe的特征：有几个？有什么属性。

# 第一种方式
# # 3、等待iframe是可用的
#
# # 4、切换操作  iframe的下标/iframe的name属性/iframe的webelement对象
# driver.switch_to.frame(4)
# driver.switch_to.frame("login_frame_qq")
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="login_frame_qq"]'))
#
# # 5、进入了iframe里面的html页面，主页面了。

# 第二种方式   iframe可用然后切进iframe  等待+切换
WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))
# 进入了iframe里面的html页面，主页面了
# 查找元素，操作元素。












