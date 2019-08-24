# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/24 16:01
# @File     : TextProBarV2.py
# @Software : web_auto_test



import time

# 文本进度条 单行动态刷新
for i in range(101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.1)