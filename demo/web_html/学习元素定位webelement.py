#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/27 0027 22:53 
# @Author : 蓝天下的风 
# @Site :  
# @File : webelement.py 
# @Software: PyCharm

from selenium import webdriver


# 1、//标签名[@属性名称=属性值]   * 匹配所有
# 2、逻辑运算 and or  //标签名[@属性名称=属性值 and 属性名称=属性值]

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_xpath('//div[@id="ul"]//a[@name="tj_login"]').click()
# driver.find_elements_by_xpath()

# 3、元素的文本内容  //标签名[text()="元素的文本内容"]  # 文本内容完全匹配

# 4、部分匹配：文本内容/属性值   contains(text()/@属性,部分值)
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