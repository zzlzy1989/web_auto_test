#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/11 0011 20:42 
# @Author : 蓝天下的风 
# @Site :  
# @File : login_datas.py 
# @Software: PyCharm
from demo.项目实战框架.PO_V1.TestDatas import Common_data as cd

# 正常登录
success_data={"user":"18684720553",
               "passwd":"python",
               "check":"{}/index/index.html".format(cd.base_url)}

wrong_datas = [
    {"user":"18684720553","passwd":"","check":"请输入密码"},
    {"user":"","passwd":"python","check":"请输入手机号码"},
    {"user":"18684","passwd":"python","check":"请输入正确的手机号码"},
    {"user":"186847205531","passwd":"python","check":"请输入正确的手机号码"}
]

# 用户名未注册、密码错误
fail_datas=[
    {"user": "19992222555", "passwd": "python", "check": "此账号没有授权，请联系管理员！"},
    {"user": "18684720553", "passwd": "python", "check": "用户名或者密码错误！"},
]