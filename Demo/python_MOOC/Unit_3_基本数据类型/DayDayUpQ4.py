# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/24 15:59
# @File     : DayDayUpQ4.py
# @Software : web_auto_test

def dayUP(df):
    dayup = 1
    for i in range(365):
       if i % 7 in [6,0]:
           dayup = dayup*(1 - 0.01)
       else:
           dayup = dayup*(1 + df)
    return dayup

dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是：{:.3f} ".format(dayfactor))



