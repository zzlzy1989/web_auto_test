#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/12/25 20:56

from Demo.PO_V4.Common.basepage import BasePage
from Demo.PO_V4.PageLocators.userPage_locator import UserPageLocator as loc

class UserPage(BasePage):

    # 获取用户余额
    def get_user_leftMoney(self):
        doc = "个人页面_获取用户余额"
        # 等待元素
        self.wait_eleVisible(loc.user_leftMoney, img_doc=doc)
        # 获取个人可用余额的文本内容
        text = self.get_element_text(loc.user_leftMoney,doc)
        # 截取数字部分 - 分隔符为 元
        return text.strip("元")

    # 获取第一条投资记录的时间、投资金额、收益金额 -- 扩展
    # def get_first_investRecord_info(self):
    #     pass