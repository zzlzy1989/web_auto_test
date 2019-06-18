# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/6/18 20:30
# @File     : basepage.py
# @Software : web_auto_test

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import logging
from demo.项目实战框架.PO_V1.Common import dir_config
import time

class BasePage:
    """
        包含了PageObjects当中，用到所有的selenium底层方法
        包含通用的一些元素操作，如alert,iframe,windows
        自己额外封装的一些web相关断言操作
        实现日志记录、失败截图
    """

    def __init__(self,driver):
        self.driver = driver

    def wait_eleVisible(self,loc,img_doc="",timeout=30,frequency=0.5):
        """
        实现了元素等待
        :param loc:
        :param img_doc:
        :param timeout:
        :param frequency:
        :return:
        """
        logging.info("等待元素{}可见。".format(loc))
        try:
            # 起始等待的时间 datetime
            start_time = datetime.datetime.now()
            # 等待元素可见
            WebDriverWait(self.driver,timeout,frequency).until(
                EC.visibility_of_element_located(loc))
            # 结束等待的时间
            end_time = datetime.datetime.now()
            # 日志记录
            logging.info("开始等待时间点:{},结束等待时间点:{},等待时长{}".
                         format(start_time,end_time,end_time-start_time))
        except:
            # 日志
            logging.exception("等待元素可见失败:")
            # 截图 - 哪一个页面哪一个操作导致的失败 + 当前时间
            self.save_web_screenshot(img_doc)
            raise

    def click_element(self,loc,img_doc,timeout=30,frequency=0.5):
        """
        实现了，等待元素可见，找元素，然后再去点击操作
        :param loc:
        :param img_doc:
        :param timeout:
        :param frequency:
        :return:
        """
        # 1、等待元素可见
        self.wait_eleVisible(loc,img_doc)
        # 2、先找元素
        ele = self.get_element(loc,img_doc)
        # 3、操作
        logging.info(" 点击元素 {}".format(loc))
        try:
            ele.click()
        except:
            logging.exception("点击元素失败")
            self.save_web_screenshot(img_doc)
            raise


    def get_element_attribute(self,loc,attr_name,img_doc):
        """
        获取元素属性值
        :param loc:
        :param attr_name:
        :param img_doc:
        :return:
        """
        ele = self.get_element(loc,img_doc)
        # 获取属性
        try:
            attr_value = ele.get_attribute(attr_name)
            logging.info("获取元素 {} 的属性 {} 值为：{}".format(loc,attr_name,attr_value))
            return attr_value
        except:
            # 日志
            logging.exception("获取元素属性失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise



    def get_element_text(self, loc, img_doc):
        """
         获取元素文本值
        :param loc:
        :param img_doc:
        :return:
        """
        ele = self.get_element(loc, img_doc)
        # 获取属性
        try:
            text = ele.text
            logging.info("获取元素 {} 文本值为：{}".format(loc, text))
            return text
        except:
            # 日志
            logging.exception("获取元素文本值失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    def input_text(self,loc,img_doc,*args):
        """
        实现了元素可见，查找，输入框操作
        :param loc:
        :param img_doc:
        :param args:
        :return:
        """
        # 1、等待元素可见
        # self.wait_eleVisible(loc,img_doc)
        # 2、先找元素
        ele = self.get_element(loc,img_doc)
        # 3、操作
        logging.info(" 给元素 {} 输入文本内容 {}".format(loc,args))
        try:
            ele.sendkeys(*args)
        except:
            logging.exception("元素输入操作失败")
            self.save_web_screenshot(img_doc)
            raise

    def get_element(self,loc,img_doc=""):
        """
        实现元素查找
        :param loc:
        :param img_doc:
        :return:
        """
        logging.info("查找{}中的元素{}".format(img_doc,loc))
        try:
            ele = self.driver.find_element(loc)
            return ele
        except:
            # 日志
            logging.exception("查找元素失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    def save_web_screenshot(self,img_doc):
        """
        实现网页截图操作
        :param img_doc:
        :return:
        """
        # 图片根目录 + 页面_功能_时间.png
        now = time.strftime("%Y%M%D%H%M%S")
        filepath="{}_{}.png".format(img_doc,now)
        try:
            self.driver.save_screenshot(dir_config.lose_dir+filepath)
            logging.info("")
        except:
            # 日志
            logging.exception("网页截图操作失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise