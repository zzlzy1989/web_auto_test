# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/24 16:01
# @File     : TextProBarV1.py
# @Software : web_auto_test

import time

# 文本进度条 简单的开始
scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束------")