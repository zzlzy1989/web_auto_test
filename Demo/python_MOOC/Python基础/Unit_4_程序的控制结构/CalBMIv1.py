# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/24 16:05
# @File     : CalBMIv1.py
# @Software : web_auto_test

while True:
    height, weight = eval(input("请输入身高(米)和体重(公斤)[逗号隔开]: "))
    bmi = weight / pow(height, 2)
    print("BMI 数值为：{:.2f}".format(bmi))
    who = ""
    if bmi < 18.5:
        who = "偏瘦"
    elif 18.5 <= bmi < 25:
        who = "正常"
    elif 25 <= bmi < 30:
        who = "偏胖"
    else:
        who = "肥胖"
    print("BMI 指标为:国际'{0}'".format(who))