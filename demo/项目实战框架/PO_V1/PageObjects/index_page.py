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

class IndexPage:

    def __init__(self,driver):
        self.driver = driver


    def check_nick_name_exists(self):
        """

        :return: 存在返回True 不存在返回False
        """
        WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located(By.XPATH,'//a[text()="关于我们"]'))

        time.sleep(0.5)

        try:
            self.driver.find_element_by_xpath('//a[text()="关于我们"]')
            return True
        except:
            return False