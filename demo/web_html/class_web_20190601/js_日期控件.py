#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/6/7 0007 12:30
# @Author : 蓝天下的风
# @Site :
# @File : study_弹框_popip_up.py
# @Software: PyCharm

# 1、允许你编辑，直接输入日期 。

# 2、只能在日历框里去选日期。不允许你直接编辑。

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 可见/视区域   -  为什么要滚动到可见区域？进行操作。

# 大部分系统在元素操作时，如果元素不在可见区域，随着操作会自动到可见区域 。

#
driver = webdriver.Chrome()


# 执行js
# js语句
js_pha = 'var a = document.getElementById("train_date");' \
         'a.readOnly = false;' \
         'a.value = "2019-07-01";' \
         'document.getElementById("search_one").click();'

driver.execute_script(js_pha)


# send_keys去输入内容，提交的时候，页面提示我内容为空？？
# dom对象去设置它的value值。 --js
