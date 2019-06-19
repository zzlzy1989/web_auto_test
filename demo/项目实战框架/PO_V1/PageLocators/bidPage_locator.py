#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/6/11 0011 21:29
# @Author : 蓝天下的风
# @Software: PyCharm

from selenium.webdriver.common.by import By

class BidPageLocator:

    #金额输入框
    money_input = (By.XPATH,"//input[contains(@class,'invest-unit-investinput')]")
    #投标按钮
    invest_button = (By.XPATH,'//button[text()="投标"]')
    #投资成功弹出框 - 查看并激活按钮
    active_button_on_successPop = (By.XPATH,'//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
    # 投资失败 - 弹出框 - 提示信息
    invest_failed_popup = (By.XPATH, '//div[contains(@class,"layui-layer-dialog")]//div[@class="text-center"]')
    # 投资失败 - 弹出框 - 关闭弹出框
    invest_close_failed_popup_button = (By.XPATH, '//div[contains(@class,"layui-layer-dialog")]//a')
