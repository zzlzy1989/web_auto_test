# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/28 14:28
# @File     : HelloWorld.py
# @Software : web_auto_test

def hello_world():
    num=eval(input())
    str_HW = "Hello World"
    length=len(str_HW)
    if num == 0:
        print(str_HW)
    elif num >0:
        for i in range(0, length, 2):
            print(str_HW[i:(i + 2)])
    else:
        for tow_str in str_HW:
            print(tow_str)

# hello_world()


def mopn():
    strmopn=input()
    print("{:.2f}".format(eval(strmopn)))

# mopn()

