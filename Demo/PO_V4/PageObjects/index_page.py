#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: index_page
# Author: 简
# Time: 2019/6/6

from Demo.PO_V4.Common.basepage import BasePage
from Demo.PO_V4.PageLocators.indexPage_locator import IndexPageLocator as loc
import time

class IndexPage(BasePage):


    # 检测昵称是否存在
    def check_nick_name_exists(self):
        """
        :return: 存在返回True,不存在返回False
        """
        self.wait_eleVisible(loc.about_us,"首页_等待关于我们元素出现")
        time.sleep(0.5)
        try:
            self.get_element(loc.user_link,"首页_找用户昵称元素")
            return True
        except:
            return False

    # 点击投标按钮
    def click_invest_button(self):
        self.click_element(loc.bid_button,"首页_点击第一个抢投标按钮")
