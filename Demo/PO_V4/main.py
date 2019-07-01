#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: main
# Author: 简
# Time: 2019/6/18

# 记录一下用例执行过程 - 日志
# 如果用例失败 - Trackback报错信息 - 失败了截图。
# 记录一下， 用例的运行时间 - 起始 - 等待的时候，等待时长。

# 用例、页面对象当中。 用例 = 页面对象 + 测试数据
# 断言失败了！！ 页面对象方法执行的时候，报错了！！

# 页面对象-任意功能 = 等待元素可见，等待元素存在、点击、输入、文本获取、属性获取、
#  alert切换、iframe切换、下拉列表、上传。。。



# 提供测试报告
import unittest
import os
from HTMLTestRunnerNew import HTMLTestRunner
from Demo.PO_V4.Common.dir_config import *

#实例化套件对象
s = unittest.TestSuite()
#TestLoader的用法
#1、实例化TestLoader对象
# 2、使用discover去找到一个目录下的所有测试用例
#3、使用s
loader = unittest.TestLoader()
s.addTests(loader.discover(testcases_dir))
# #运行
# runner = unittest.TextTestRunner()
# runner.run(s)

fp = open(htmlreport_dir + '/autoTest_report.html', 'wb')
runner = HTMLTestRunner(
            stream=fp,
            title='单元测试报告',
            description='单元测试报告',
            tester="小简"
            )
runner.run(s)

