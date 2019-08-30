# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/28 17:34
# @File     : 第五章测验.py
# @Software : web_auto_test

# def func(a,b):
#   c=a**2+b
#   b=a
#   return c
# a=10
# b=100
# c=func(a,b)+a
# print(c)


"""
随机密码生成
描述
补充编程模板中代码，完成如下功能：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

以整数17为随机数种子，获取用户输入整数N为长度，产生3个长度为N位的密码，密码的每位是一个数字。每个密码单独一行输出。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

产生密码采用random.randint()函数。
"""

#请在...补充代码
# import random
#
# def genpwd(length):
#
#     a = 10**(length-1)
#     b = 10**length-1
#     return random.randint(a,b)
#
#
# length = eval(input())
#
# random.seed(17)
# for i in range(3):
#     print(genpwd(length))



"""
连续质数计算
描述
补充编程模板中代码，完成如下功能：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

获得用户输入数字N，计算并输出从N开始的5个质数，单行输出，质数间用逗号,分割。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

注意：需要考虑用户输入的数字N可能是浮点数，应对输入取整数；最后一个输出后不用逗号。
"""



def prime(m):
    if m <= 1:
        return False
    elif m == 2:
        return True
    else:
        for i in range(2, m):
            if m % i == 0:
                return False
        else:
            return True


m = eval(input())
count = 1
if "." in str(m):
    m = round(m)+1
else:
    m=m
while True:
    if count <= 5:
        if prime(m):
            if count < 5:
                print(m, end=",")
            else:
                print(m)
            count += 1
        m += 1
    else:
        break