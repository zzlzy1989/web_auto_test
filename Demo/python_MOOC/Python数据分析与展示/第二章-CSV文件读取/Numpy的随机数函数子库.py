# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/31 16:34
# @File     : Numpy的随机数函数子库.py
# @Software : web_auto_test

'''
NumPy的随机数函数子库

NumPy的random子库
    np.random.*
    np.random.randn()
    np.random.rand()
    np.random.randint()

# NumPy直接提供的统计类函数
    # np.*
    # np.std() np.var() np.average()
'''

import numpy as np

# a = np.random.rand(3,4,5)
# print(a)
# sn = np.random.randn(3,4,5)
# print(sn)

# rand(d0, d1,.., dn)           根据d0‐dn创建随机数数组，浮点数，[0, 1)，均匀分布
# randn(d0, d1,.., dn)          根据d0‐dn创建随机数数组，标准正态分布
# randint(low[, high, shape])   根据shape创建随机整数或整数数组，范围是[low, high)
# seed(s)
# 随机数种子，s是给定的种子值
# b = np.random.randint(100,200,(3,4))
# print(b)
# np.random.shuffle(b)
# print(b)
# np.random.shuffle(b)
# print(b)

# shuffle(a)
# 根据数组a的第1轴进行随排列，改变数组x
# permutation(a)
# 根据数组a的第1轴产生一个新的乱序数组，不改变数组x
# choice(a[, size, replace, p])  从一维数组a中以概率p抽取元素，形成size形状新数
# replace表示是否可以重用元素，默认为False
# np.random.permutation(b)
# print(b)

# 函数 说明
# uniform(low,high,size) 产生具有均匀分布的数组,low起始值,high结束值,size形状
# normal(loc,scale,size) 产生具有正态分布的数组,loc均值,scale标准差,size形状
# poisson(lam,size) 产生具有泊松分布的数组,lam随机事件发生率,size形状

# NumPy直接提供的统计类函数
# np.*
# np.std() np.var() np.average()

# sum(a, axis=None) 根据给定轴axis计算数组a相关元素之和，axis整数或元组
# mean(a, axis=None) 根据给定轴axis计算数组a相关元素的期望，axis整数或元组
# average(a,axis=None,weights=None) 根据给定轴axis计算数组a相关元素的加权平均值
# std(a, axis=None) 根据给定轴axis计算数组a相关元素的标准差
# var(a, axis=None 根据给定轴axis计算数组a相关元素的方差
# axis=None 是统计函数的标配参数

a = np.arange(15).reshape(3,5)
print("a 的值:\n{}".format(a))
print("根据给定轴axis计算数组a相关元素之和，axis整数或元组 的值:\n{}".format(np.sum(a)))
print("根据给定轴axis计算数组a相关元素的期望，axis整数或元组 的值:\n{}".format(np.mean(a,axis=1)))
print("根据给定轴axis计算数组a相关元素的期望，axis整数或元组 的值:\n{}".format(np.mean(a,axis=0)))
print("根据给定轴axis计算数组a相关元素的加权平均值 的值:\n{}".format(np.average(a,axis=0,weights=[10,5,1])))
print("根据给定轴axis计算数组a相关元素的标准差 的值:\n{}".format(np.std(a)))
print("根据给定轴axis计算数组a相关元素的方差 的值:\n{}".format(np.var(a)))

# min(a) max(a) 计算数组a中元素的最小值、最大值
# argmin(a) argmax(a) 计算数组a中元素最小值、最大值的降一维后下标
# unravel_index(index, shape) 根据shape将一维下标index转换成多维下标
# ptp(a) 计算数组a中元素最大值与最小值的差
# median(a) 计算数组a中元素的中位数（中值）
b = np.arange(15,0,-1).reshape(3,5)
print("b 的值：\n{}".format(b))
print("计算数组a中元素的最小值、最大值 的值：\n{}".format(np.max(b)))
print("计算数组a中元素最小值、最大值的降一维后下标 的值：\n{}".format(np.argmax(b)))
print("根据shape将一维下标index转换成多维下标 的值：\n{}".format(np.unravel_index(np.argmax(b),b.shape)))
print("计算数组a中元素最大值与最小值的差 的值：\n{}".format(np.ptp(b)))
print("计算数组a中元素的中位数（中值） 的值：\n{}".format(np.median(b)))


# NumPy的梯度函数
# np.gradient(f) 计算数组f中元素的梯度，当f为多维时，返回每个维度梯度
# 梯度：连续值之间的变化率，即斜率
# XY坐标轴连续三个X坐标对应的Y轴值：a, b, c，其中，b的梯度是： (c‐a)/2
c = np.random.randint(0,20,(5))
print(c)
print(np.gradient(c))

d = np.random.randint(0,20,(5))
print(d)
print(np.gradient(d))

e = np.random.randint(0,50,(3,5))
print(e)
print(np.gradient(e))


"""
小结
    CSV文件
    np.loadtxt()
    np.savetxt()
    多维数据存取
    a.tofile() np.fromfile()
    np.save() np.savez() np.load()
    随机函数
    np.random.rand() np.random.randn()
    np.random.randint() np.random.seed()
    np.random.shuffle() np.random.permutation()
    np.random.choice()NumPy的统计函数
    np.sum()
    np.mean()
    np.average()
    np.std()
    np.var()
    np.median()
    np.min()
    np.max()
    np.argmin()
    np.argmax()
    np.unravel_index()
    np.ptp()
    NumPy的梯度函数
    np.gradient()
"""