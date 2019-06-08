#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/8 0008 15:34 
# @Author : 蓝天下的风 
# @Site :  
# @File : home_work_0527.py 
# @Software: PyCharm

"""
    0、使用帐号和密码登陆课堂派。
    1、进入你所在的班级，随机选择一个已提交的作业(带有"查看成绩"的作业)，查看你的成绩是多少
    2、获取1中作业下，作业被分享的同学名称。
    3、在1中，切换到作业讨论，并发表你的评论。
    4、点击【同学】，在同学当中，随便选一个学生，向其发送消息（鼠标悬浮后，发消息图标才出现）。
    5、在4的【同学】当中，使用右上角搜索功能。输入任意一个学生id，搜索学生信息。
    【进阶思考：设计一条测试用例，来确认你的搜索结果与期望的匹配。使用unittest哦！！】
    ps：代码连接运行5次都通过的情况下，才算比较稳定。提交上来的代码，一定要是自己运行通过的。

    # 登录页面
    # 首页 // a[contains(text(), "首页")]
    # 移动端 //a[contains(text(),"移动端")]
    # 解决方案 // a[text() = "解决方案"]
    # 会员权益 //a[text()="解决方案"]/parent::div/following-sibling::a[text()="会员权益"]
    # 帮助中心 // a[text() = "解决方案"]/parent::div/following-sibling::a[text()="帮助中心"]
    # 媒体报道标黑的标题 //div[@id="section-words"]/ul/li[@class="mrli mainli"and@index="1"]/div/a
    # 底部-关于我们 //div[@class="footer"]//a[contains(text(),"关于我们")]
    # 底部-联系我们 //div[@class="footer"]//a[text()="联系我们"]
    # 底部-服务条款 //div[@class="footer"]//a[text()="联系我们"]/following-sibling::a[text()="服务条款"]
    # 底部-浏览器下载 //div[@class="footer"]//a[text()="更新动态"]/preceding-sibling::a[contains(text(),"浏览器")]
    # 底部-更新动态 //div[@class="footer"]//a[text()="更新动态"]
    # 登录 //div[@id="indextop"]//a[@class="login"]
    # 注册 //div[@id="indextop"]//a[@class="regist"]
    # 账号登录标签 //div[@id="indextop"]//following-sibling::div[@class="reg-log"]//div[@class="title items"]/a[contains(text(),"账号登录")]
    # 账号登录：用户名  //input[@name="account"]
    # 账号登录：密码   //input[@name="pass"]
"""


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest

class TestKtp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ketangpai.com/")

    def setDown(self):
        self.driver.quit()

    def test_login_success(self):

        WebDriverWait(self.driver,30).until(
            EC.visibility_of_element_located((
                By.XPATH,'//div[@id="indextop"]//a[@class="login"]')))
        self.driver.find_element_by_xpath('//div[@id="indextop"]//a[@class="login"]').click()

        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,'//input[@name="account"]')))
        self.driver.find_element_by_xpath('//input[@name="account"]').send_keys("394845369@qq.com")
        self.driver.find_element_by_xpath('//input[@name="pass"]').send_keys("qwe@1234")
        # 账号登录：下次自动登录
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,'//input[@name="pass"]/parent::div/following-sibling::div[@class="opt clearfix"]/a[contains(text(),"下次自动登录")]')))
        get_attr=self.driver.find_element_by_xpath('//input[@name="pass"]/parent::div/following-sibling::div[@class="opt clearfix"]/a[contains(text(),"下次自动登录")]')\
            .get_attribute("class")
        if get_attr=="auto-login fl active":
            self.driver.find_element_by_xpath('//input[@name="pass"]/parent::div/following-sibling::div[@class="opt clearfix"]/a[contains(text(),"下次自动登录")]').click()
        # 账号登录--登录按钮 //input[@name="pass"]/parent::div/following-sibling::a[contains(text(),"登录")]
        self.driver.find_element_by_xpath('//input[@name="pass"]/parent::div/following-sibling::a[contains(text(),"登录")]').click()





        sleep(15)
        self.driver.quit()



