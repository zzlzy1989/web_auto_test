#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/6/11 0011 21:29
# @Author : 蓝天下的风
# @Software: PyCharm
import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir =  os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"TestCases")


# 生成报告存放地址
htmlreport_dir =  os.path.join(base_dir,"Outputs/reports")

# 生成日志存放地址
logs_dir =  os.path.join(base_dir,"Outputs/logs")

# config_dir =  os.path.join(base_dir,"Config")
# 截图地址
screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")
print(screenshot_dir)