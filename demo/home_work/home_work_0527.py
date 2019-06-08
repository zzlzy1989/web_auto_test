#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/8 0008 15:34 
# @Author : 蓝天下的风 
# @Site :  
# @File : home_work_0527.py 
# @Software: PyCharm

"""
    ===元素定位练习+等待===课堂派系统当中，你能看到的元素都定位一下==用我们上课讲的内容===
    格式：#备注（哪个页面哪个元素）
    定位代码多复习一下等待的用法。...

    Xpath常用轴定位和文本定位
    1、preceding-sibling: 哥哥姐姐
        following-sibling：弟弟妹妹
        //a[@name="tj_trvideo"]/following-sibling::a[@name="tj_login"]
        //a[@name="tj_settingicon"]/preceding-sibling::a[@name="tj_login"]
    2、爸爸：parent   祖先：ancestor
        //a[@name="tj_trtieba"]/parent::div/a[@name="tj_login"]
        //a[text()="百度首页"]/parent::div/following-sibling::div//a[@name="tj_login"]
    3、//标签名[contains(text(),"部分文本内容")]  # 太长了
        //标签名[contains(@属性,"部分属性值")]   # id(不变动+变动) # class有多个。
    4、层级定位  第一种方式
        后一条件，是在前一个得到的结果之内去搜索。//条件1//条件2.....
        //div[@id="u1"]//a[@name="tj_login"]
    等待
    1、 智能等待：明确的条件（元素可见，窗口存在）。等待+条件（如果你10秒出现了，我就开始下一步操作。）
        元素存在（html里面，能找到）；
        元素可见（存在并且可见-看得见大小-可见才可操作）；
        元素可用（可见之后，才有可用的可能性。只读/不可点击-不可用）
        WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="首页"]')))
    2、隐性等待
        智能等待：如果你10秒出现了，我就开始下一步操作。   设置上限：30秒 超时TimeoutException    
        implicitly_wait():隐式等待
	    driver.implicitly_wait(30)
	3、傻傻的等待
	    import time
	    time.sleep(30)
"""


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class FindElement:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ketangpai.com/")

    def login_page(self):
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
        WebDriverWait(self.driver,30).until(
            EC.visibility_of_element_located((
                By.XPATH,'//div[@id="indextop"]//a[@class="login"]')))
        self.driver.find_element_by_xpath('//div[@id="indextop"]//a[@class="login"]').click()

        # 账号登录标签 //div[@id="indextop"]//following-sibling::div[@class="reg-log"]//div[@class="title items"]/a[contains(text(),"账号登录")]
        # 账号登录：用户名  //input[@name="account"]
        # 账号登录：密码   //input[@name="pass"]
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

if __name__ == '__main__':
    find_element = FindElement()
    find_element.login_page()


