#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: ele_locator
# Author: 简
# Time: 2019/5/25

from selenium import webdriver

# 元素的特征  属性

# 8种 定位方式
# 6种   通过一个属性来定位的
# 2种   组合各种属性来定位 + 结合各种关系来定位

# //*[@id="kw"]
# /html/body/div[2]/div/form/div[1]/input


# 开启跟google的一个会话
driver = webdriver.Chrome()
# 访问一个网址
driver.get("http://www.baidu.com")
# 1、通过元素的id属性找元素  # kw1234567
ele = driver.find_element_by_id("kw")   # 返回的WebElement对象 封装了元素的属性和操作
# print(ele.tag_name)
# print(ele.get_attribute("class"))

# 2、name属性
driver.find_element_by_name("wd")   # 找一个单一的元素。从上往下，符合条件的第一个
ele_list = driver.find_elements_by_name("wd")  # 找到所有匹配的元素。#返回的是列表，每一个都是WEbElement
print(ele_list[0].tag_name)

# 3、class属性  -- 只能选择一个class值
# driver.find_element_by_class_name()
# driver.find_elements_by_class_name()

# 4、标签名 tag_name
# driver.find_element_by_tag_name()
# driver.find_elements_by_tag_name()

# 5,6  链接元素  link  text  #完全匹配  # 模糊匹配
# driver.find_element_by_link_text("更多产品")  # 完全匹配
# driver.find_element_by_partial_link_text("更多")   # 模糊匹配

# 7,8  xpath=易懂    css=难懂

# xpath定位

# 绝对定位   严格按照路径和位置来定位元素  以/开头     父/子关系
# 相对定位   参照物：整个html    只要能够在这个页面当中，找到符合属性的元素。
#             以//开头

# //*[@id="kw"]
# /html/body/div[2]/div/form/div[1]/input
# //input[@name="phone"]

# 1、//标签名[@属性名称=属性值]  * 匹配所有
# 2、逻辑运算   and or    //标签名[@属性名称=属性值 and @属性名称=属性值]

driver.find_element_by_xpath('//input[@name="phone"]')  #
# driver.find_elements_by_xpath()

# 3、元素的文本内容  //标签名[text()="元素的文本内容"]  # 文本内容完全匹配

#  4、部分匹配：文本内容/属性值   contains(text()/@属性,部分值)
#       //标签名[contains(text(),"部分文本内容")]  # 太长了
#       //标签名[contains(@属性,"部分属性值")]   # id(不变动+变动) # class有多个。


# 5、当你不能通过自己的属性唯一找到的时候，就要利用层级关系 。
# 5.1、层级定位  第一种方式
#     后一条件，是在前一个得到的结果之内去搜索。//条件1//条件2.....
      #  //div[@id="u1"]//a[@name="tj_login"]

# 5.2 层级定位 - 轴定位    # 表达式   /轴定位名称::标签名[属性表达]
      # 兄弟姐妹  -  直系的   有比你大的，有比你小的。
      # preceding-sibling: 哥哥姐姐
      # following-sibling：弟弟妹妹
      # //a[@name="tj_trvideo"]/following-sibling::a[@name="tj_login"]
      # //a[@name="tj_settingicon"]/preceding-sibling::a[@name="tj_login"]

      # 爸爸：parent   祖先：ancestor
      # //a[@name="tj_trtieba"]/parent::div/a[@name="tj_login"]
      # //a[text()="百度首页"]/parent::div/following-sibling::div//a[@name="tj_login"]










