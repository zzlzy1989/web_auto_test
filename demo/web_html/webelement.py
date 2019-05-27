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
# driver.find_element_by_xpath()

# 3、元素的文本内容 //标签名[text()="元素的文本内容"] #文本内容完全匹配

# 部分匹配:文本内容/属性值  contains(text()/@属性，部分值)
#   //标签名[contains(text(),"部分属性值")] #太长了，使用contains
#   //标签名[contains(@属性,"部分属性值")]    #id(不变动+变动) #class值-

# 4、当你不能通过自己的属性唯一找到的时候，就要利用层级关系
# 4.1 层级定位 第一种方式
#    后一个条件是前一个得到的结果之内去搜索   //条件1//条件2//条件3
#    //div[@id="ul"]//a[@name="tj_login"]

# 4.2 层级定位   表达式 轴定位名称::标签名[@属性=值]
        # 兄弟姐妹 - 直系的    有比你大的，有比你小的
        # preceding-sibling:哥哥姐姐
        # following-sibling:弟弟妹妹
        # //a[@name="tj_trvideo"]/following-sibling::a[@name="tj_login"]
        # //a[@name="tj_trvideo"]/following-sibling::a[@name="tj_login"]