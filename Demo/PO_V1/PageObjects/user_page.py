#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/6/11 0011 21:29
# @Author : 蓝天下的风
# @Software: PyCharm

from Demo.PO_V1 import BasePage
from Demo.PO_V1.PageLocators import UserPageLocator as loc

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