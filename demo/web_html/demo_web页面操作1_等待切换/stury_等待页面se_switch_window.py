#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: se_switch_window
# Author: 简
# Time: 2019/5/28



from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


"""
    implicitly_wait():隐式等待
    当使用了隐士等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
    换句话说，当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0
    一旦设置了隐式等待，则它存在整个 WebDriver 对象实例的声明周期中，隐式的等到会让一个正常响应的应用的测试变慢，
    它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间。
"""

# 浏览器会话的开始
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")  # 静态页面加载完成

# 设置全局等待时间
driver.implicitly_wait(30)

# 输入柠檬班并点击百度一下
driver.find_element_by_id("kw").clear()  # 清除文本
driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()
# 等待
locator = (By.XPATH,'//a[text()="_腾讯课堂"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))

# 柠檬班-腾讯课堂
driver.find_element_by_xpath('//a[text()="_腾讯课堂"]').click()


# 方式二
# step1: 获取窗口数
handles = driver.window_handles   # 只有1个窗口。
# step2: 执行打开新窗口的操作 -
driver.find_element(*locator).click()   # 本操作带来了新窗口的出现 -》 2

# step3: 确认新的窗口出现了，我再去操作它。等待新窗口出现。
# EC.new_window_is_opened  # 比窗口总数的大小。# 传一个窗口总数。
WebDriverWait(driver,10).until(EC.new_window_is_opened(handles))  # 2 > 1 # 确认新窗口出现
# step4: 再次获取 窗口的handles
handles = driver.window_handles   # 2个窗口
# step5: 切换 到新窗口
driver.switch_to.window(handles[-1])

# 方式一
# # 打开新的窗口
# # 1、获取所有的窗口
# handles = driver.window_handles
# print(handles)  # 按照窗口出现的顺序。最后一个就是最近打开的窗口。
# # 当前窗口的handle
# print(driver.current_window_handle)
# # 2、切换新的窗口
# driver.switch_to.window(handles[-1])
# print("切换之后的窗口为：",driver.current_window_handle)


# 新的窗口当中，点击  课程
# 等待
locator = (By.XPATH,'//section[@class="section-main"]//h2[contains(text(),"课程")]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
driver.find_element(*locator).click()

