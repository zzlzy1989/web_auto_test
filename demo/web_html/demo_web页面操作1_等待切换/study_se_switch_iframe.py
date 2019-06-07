#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/6 0006 19:30 
# @Author : 蓝天下的风 
# @Site :  
# @File : study_se_switch_iframe.py 
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://ke.qq.com/")
driver.find_element_by_xpath('//*[@id="js-mod-header-login"]//a[text()="登录"]').click()


# 1、html里面再嵌套一个 html
# 2、DOM --- 只针对一个HTML   id,xpath
# *******************方式一***********************
# 3、如果你要操作元素，在iframe当中，切换

# 4、确认iframe的特征：有几个？有什么属性

# 5、等待iframe是可用的

# 6、切换操作   frame支持3中传参，index,iframe的name属性,iframe的webelement对象
driver.switch_to.frame("login_frame_qq")
driver.switch_to.frame(4)
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="login_frame_qq"]'))
# 7、进入了iframe页面的html页面，主页面
driver.find_element_by_xpath('//a[@class="face"]//img[@id="img_394845369"]').click()



# *******************方式二***********************
# 1、iframe 可用然后切进iframe,  等待+切换
WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))
# 2、进入了iframe页面的html页面，主页面
# 3、查找元素，操作元素

# 如何从iframe 中切换出来
driver.switch_to.default_content()

# 上一个iframe
driver.switch_to.parent_frame()


