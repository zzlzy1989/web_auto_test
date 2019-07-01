#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/11/28 17:04

import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir =  os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"TestCases")



htmlreport_dir =  os.path.join(base_dir,"Outputs/reports")

logs_dir =  os.path.join(base_dir,"Outputs/logs")

# config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")
print(screenshot_dir)