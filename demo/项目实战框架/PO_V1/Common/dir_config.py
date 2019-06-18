#-*-coding:utf-8-*-
#@Time      :2019/5/1 0001 22:39
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@Software  :PyCharm Community Edition

import os

#定义到项目根路径
absolute_path = os.path.abspath(__file__)
#获取觉得路径的上一级目录
up_one_ath = os.path.dirname(absolute_path)
#获取上一级目录的上一级目录
up_two_ath = os.path.dirname(up_one_ath)
base_dir = up_two_ath

#测试用例文件地址
case_file = os.path.join(base_dir,'TestDatas','cases.xlsx')
#设置全局配置文件地址
global_file = os.path.join(base_dir,'config','global.conf')
#线上测试环境地址
online_file = os.path.join(base_dir,'config','online.conf')
#测试环境地址
test_file = os.path.join(base_dir,'config','test.conf')
#日志文件的地址
log_dir = os.path.join(base_dir, 'Log')
#测试用例路径地址
case_dir = os.path.join(base_dir, 'Testcases')
#测试报告路径地址
report_dir = os.path.join(base_dir, 'Reports')
# 失败截图路径地址
lose_dir = os.path.join(base_dir, 'Reports/screenshots')
