#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/6 0006 21:48 
# @Author : 蓝天下的风 
# @Site :  
# @File : index_page.py 
# @Software: PyCharm

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from Demo.项目实战框架.PO_V1.PageLocators.indexPage_locator import IndexPageLocator as loc
from Demo.项目实战框架.PO_V1.Common.basepage import BasePage

class IndexPage(BasePage):

    def check_nick_name_exists(self):
        """
            :return: 存在返回True 不存在返回False
        """
        WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located((By.XPATH,'//a[text()="关于我们"]')))

        time.sleep(0.5)

        try:
            self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]')
            return True

        except:
            return False

    # 点击投标按钮

    def click_invest_button(self):
        self.click_element(loc.bid_button, "首页_点击第一个抢投标按钮")
