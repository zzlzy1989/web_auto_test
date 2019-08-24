# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/24 16:05
# @File     : CalBMIv2.py
# @Software : web_auto_test



while True:
    height, weight = eval(input("请输入身高(米)和体重\(公斤)[逗号隔开]: "))
    bmi = weight / pow(height, 2)
    print("BMI 数值为：{:.2f}".format(bmi))
    nat = ""
    if bmi < 18.5:
        nat = "偏瘦"
    elif 18.5 <= bmi < 24:
        nat = "正常"
    elif 24 <= bmi < 28:
        nat = "偏胖"
    else:
        nat = "肥胖"
    print("BMI 指标为:国内'{0}'".format(nat))