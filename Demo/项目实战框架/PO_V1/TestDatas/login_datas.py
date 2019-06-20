#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/11 0011 20:42 
# @Author : 蓝天下的风 
# @Site :  
# @File : login_datas.py 
# @Software: PyCharm
from Demo.项目实战框架.PO_V1.TestDatas import Common_Datas as cd

# 正常登录
success_data={"user":"18684720553",
               "passwd":"python",
               "check":"{}/Index/index".format(cd.base_url)}


wrong_datas = [
    {"user":"18684720553","passwd":"","check":"请输入密码"},
    {"user":"","passwd":"python","check":"请输入手机号"},
    {"user":"186847","passwd":"python","check":"请输入正确的手机号"},
    {"user":"186847055311","passwd":"python","check":"请输入正确的手机号"}
]

# 用户名未注册 /密码错误
fail_datas = [
    {"user":"18600000000","passwd":"pthon","check":"此账号没有经过授权，请联系管理员!"},
    {"user":"18684720553","passwd":"pthon111","check":"帐号或密码错误!"}
]