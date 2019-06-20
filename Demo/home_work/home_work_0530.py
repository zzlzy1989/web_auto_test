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
import random
from selenium.webdriver.common.keys import Keys


class TestKtp(unittest.TestCase):

    def setUp(self):
        self.username = "394845369@qq.com"
        self.password = "*******"
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ketangpai.com/")
        self.driver.maximize_window() # 窗口最大化
        self.driver.implicitly_wait(20)

    def setDown(self):
        sleep(15)
        self.driver.quit()

    def test_inclass(self):
        #  使用帐号和密码登陆课堂派。
        WebDriverWait(self.driver,30).until(
            EC.visibility_of_element_located((
                By.XPATH,'//div[@id="indextop"]//a[@class="login"]')))
        self.driver.find_element_by_xpath('//div[@id="indextop"]//a[@class="login"]').click()

        WebDriverWait(self.driver,30).until(
            EC.visibility_of_element_located((
                By.XPATH,'//input[@name="account"]')))
        self.driver.find_element_by_xpath('//input[@name="account"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//input[@name="pass"]').send_keys(self.password)
        # 账号登录：下次自动登录
        WebDriverWait(self.driver,30).until(
            EC.visibility_of_element_located((
                By.XPATH,'//input[@name="pass"]/parent::div/following-sibling::div[@class="opt clearfix"]/a[contains(text(),"下次自动登录")]')))
        get_attr=self.driver.find_element_by_xpath('//input[@name="pass"]/parent::div/following-sibling::div[@class="opt clearfix"]/a[contains(text(),"下次自动登录")]')\
            .get_attribute("class")
        if get_attr=="auto-login fl active":
            self.driver.find_element_by_xpath('//input[@name="pass"]/parent::div/following-sibling::div[@class="opt clearfix"]/a[contains(text(),"下次自动登录")]').click()

        # 账号登录--登录按钮 //input[@name="pass"]/parent::div/following-sibling::a[contains(text(),"登录")]
        self.driver.find_element_by_xpath('//input[@name="pass"]/parent::div/following-sibling::a[contains(text(),"登录")]').click()

        # 如果有公告弹框，则需要关闭公告弹框 （注意弹框的ID带数字，考虑id是变动的）
        try:
            close_ele = self.driver.find_element_by_xpath('//*[contains(@class,"layui-layer-page")]//div[@class="pop-title"]//a')
        except:
            pass
        else:
            close_ele.click()

        # 进入你所在的班级，随机选择一个已提交的作业(带有"查看成绩"的作业)，查看你的成绩是多少
        locator = (By.XPATH,'//div[@id="viewer-container-lists"]//a[contains(text(),"Python全栈第15期")]')
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

        # 点击【同学】，在同学当中，随便选一个学生，向其发送消息（鼠标悬浮后，发消息图标才出现）。
        locator = (By.XPATH,'//a[text()="查看成绩"]')
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(locator))
        score_eles = self.driver.find_elements(*locator) # 获取到所有的查看元素，保存在变量中
        index = random.randint(0,len(score_eles)-1) # 随机选择一个【查看成绩】的元素进入
        score_eles[index].click()

        # 查看你的成绩是多少
        locator = (By.XPATH,'//p[contains(@class,"score")]//span')
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(locator))
        score = self.driver.find_element(*locator).text
        print("随机找到一个作业，查看成绩为：{}".format(score))

        # 获取1中作业下，作业被分享的同学名称。
        stu_eles = self.driver.find_elements_by_xpath('//p[@class="share-name"]')
        print("本次分享的学员，昵称为：")
        for ele in stu_eles:
            print(ele.text)

        # 在1中，切换到作业讨论，并发表你的评论。
        self.driver.find_element_by_xpath('//div[@id="third-nav"]/a[contains(text(),"作业讨论")]').click()
        locator = (By.XPATH,'//div[contains(@class,"input-click")]') # 点击出现输入区域
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

        commit_text = (By.XPATH,'//textarea[@class="comment-txt"]')
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((commit_text)))
        self.driver.find_element(*commit_text).send_keys("作业已提交，大家都做的非常好！")
        self.driver.find_element_by_xpath('//div[@class="add-comment"]//a[text()="确定"]').click()


        # 点击【同学】，在同学当中，随便选一个学生，向其发送消息（鼠标悬浮后，发消息图标才出现）。
        self.driver.find_element_by_xpath('//*[@id="return-course"]').click() # 返回班级首页

        stu_loc = (By.XPATH,'//a[text()="同学"]')
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(stu_loc))
        self.driver.find_element(*stu_loc).click() # 点击同学，进入学员页面

        # 点击全部同学
        all_stu = (By.XPATH,'//li[contains(text(),"全部学生")]')
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(all_stu))
        self.driver.find_element(*all_stu).click()

        # 学生列表-随机选择一个同学进行发消息
        stu_loc = (By.XPATH,'//div[@class="all-list"]//p[@class="studentavatar"]')
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(stu_loc))
        sleep(1) # 有多个列表元素，第一个出现后，需要再等其他的元素出现。

        stu_eles = self.driver.find_elements_by_xpath('//div[@class="all-list"]//li')
        index = random.randint(5,len(stu_eles)-1)
        print(index)
        stu_mail = stu_eles[index].find_element_by_class_name('mail').get_attribute("title")
        print(stu_mail)
        stu_eles[index].click()
        sleep(2)
        self.driver.save_screenshot('save_screenshot.png') # 截屏

        # 发消息标志框的定位表达
        print('//div[@class="all-list"]//li//p[@title="{}"]/following-sibling::a'.format(stu_mail))
        ee = self.driver.find_element_by_xpath(
            '//div[@class="all-list"]//li//p[@title="{}"]/following-sibling::a'.format(stu_mail))  # 找子元素
        # 鼠标悬浮操作 并点击
        ActionChains(self.driver).move_to_element(ee).click(ee).perform()  # 鼠标操作。

        # ee.click() # 点击聊天标志
        # ElementNotVisibleException: Message: element not interactable
        msg = (By.XPATH, '//textarea[@class="ps-container"]')
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(msg))
        self.driver.find_element(*msg).send_keys("我是蓝天下的风，给你发消息很抱歉，做作业测试，勿回，谢谢！", Keys.CONTROL, Keys.ENTER)
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[contains(@id,"layui-layer")]//span[@class="layui-layer-setwin"]/a')))
        self.driver.find_element_by_xpath('//div[contains(@id,"layui-layer")]//span[@class="layui-layer-setwin"]/a').click()


        # 在4的【同学】当中，使用右上角搜索功能。输入任意一个学生id，搜索学生信息。
        # 进入你所在的班级，随机选择一个已提交的作业(带有"查看成绩"的作业)，查看你的成绩是多少
        locator = (By.XPATH,'//a[@id="return-course"]')
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()
        # 点击同学链接，进入学员页面
        stu_loc = (By.XPATH, '//a[text()="同学"]')
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(stu_loc))
        self.driver.find_element(*stu_loc).click()

        search_loc = (By.XPATH, "//div[contains(@class,'input-box')]")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(search_loc))

        search_ele = self.driver.find_element_by_xpath("//div[contains(@class,'input-box')]//input")
        search_ele.send_keys("1575", Keys.ENTER)
        self.driver.save_screenshot("搜索的学生信息.png")


if __name__ == '__main__':
    TestKtp=TestKtp()
    TestKtp.test_inclass()
