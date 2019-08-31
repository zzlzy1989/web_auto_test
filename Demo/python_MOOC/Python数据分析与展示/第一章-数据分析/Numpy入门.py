# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/30 11:06
# @File     : Numpy入门.py
# @Software : web_auto_test

"""
Python数据分析与展示
掌握表示、清洗、统计和展示数据的能力

NumPy
1、N维数据
    一维数据
    一组数据的有序结构

    二维数据
    二维数据由多个一维数据构成，是一维数据的组合形式
        表格是典型的二维数据
        其中，表头是二维数据的一部分

    多维数据
    多维数据由一维或二维数据在新维度上扩展形

    高维数据
    高维数据仅利用最基本的二元关系展示数据间的复杂结构
        键值对，JSON串

    数据维度的Python表示
    一维数据：列表和集合类型    [3.1398, 3.1349, 3.1376] 有序
                            {3.1398, 3.1349, 3.1376} 无序

    数据维度是数据的组织形式
            [ [3.1398, 3.1349, 3.1376],
            [3.1413, 3.1404, 3.1401] ]
    二维数据：列表类型
    多维数据：列表类型

    高维数据：字典类型 或 数据表示格式 JSON、XML和YAML格式

2、NumPy是SciPy、Pandas等数据处理或科学计算库的基础
    • 一个强大的N维数组对象 ndarray
    • 线性代数、傅里叶变换、随机数生成等功能
    N维数组对象：ndarray
        ndarray是一个多维数组对象，由两部分构成：
        • 实际的数据
        • 描述这些数据的元数据（数据维度、数据类型等）
        ndarray数组一般要求所有元素类型相同（同质），数组下标从0开始

    ndarray数组创建方法
    （1）从Python中的列表、元组等类型创建ndarray数组
        x = np.array(list/tuple)
        x = np.array(list/tuple, dtype=np.float32)  可以直接设置ndarray类型
        当np.array()不指定dtype时，NumPy将根据数据情况关联一个dtype类型
    （2）使用NumPy中函数创建ndarray数组，如：arange, ones, zeros等
        函数                  说明
        np.arange(n)        类似range()函数，返回ndarray类型，元素从0到n‐1
        np.ones(shape)      根据shape生成一个全1数组，shape是元组类型
        np.zeros(shape)     根据shape生成一个全0数组，shape是元组类型
        np.full(shape,val)  根据shape生成一个数组，每个元素值都是val
        np.eye(n)           创建一个正方的n*n单位矩阵，对角线为1，其余为0

        np.ones_like(a) 根据数组a的形状生成一个全1数组
        np.zeros_like(a) 根据数组a的形状生成一个全0数组
        np.full_like(a,val) 根据数组a的形状生成一个数组，每个元素值都是val
    （3）使用NumPy中其他函数创建ndarray数组
        函数                  说明
        np.linspace()       根据起止数据等间距地填充数据，形成数组
        np.concatenate()    将两个或多个数组合并成一个新的数组

    ndarray数组的维度变换
        方法                  说明
        .reshape(shape)     不改变数组元素，返回一个shape形状的数组，原数组不变
        .resize(shape)      与.reshape()功能一致，但修改原数组
        .swapaxes(ax1,ax2)  将数组n个维度中两个维度进行调换
        .flatten()          对数组进行降维，返回折叠后的一维数组，原数组不变

    ndarray数组向列表的转换
        ls = a.tolist()

    数组的索引和切片
        一维数组的索引和切片：与Python的列表类似

    数组与标量之间的运算
        数组与标量之间的运算作用于数组的每一个元素

    NumPy一元函数
    对ndarray中的数据执行元素级运算的函数
        函数                          说明
        np.abs(x) np.fabs(x)    计算数组各元素的绝对值
        np.sqrt(x)              计算数组各元素的平方根
        np.square(x)            计算数组各元素的平方
        np.log(x) np.log10(x)
        np.log2(x)              计算数组各元素的自然对数、10底对数和2底对
        np.ceil(x) np.floor(x)  计算数组各元素的ceiling值 或 floor值
        np.rint(x)              计算数组各元素的四舍五入值
        np.modf(x)              将数组各元素的小数和整数部分以两个独立数组形式返回
        np.cos(x) np.cosh(x
        np.sin(x) np.sinh(x)
        np.tan(x) np.tanh(x)    计算数组各元素的普通型和双曲型三角函数
        np.exp(x)               计算数组各元素的指数值
        np.sign(x)              计算数组各元素的符号值，1(+), 0, ‐1(‐)

    NumPy二元函数
        函数                              说明
        + ‐ * / **                      两个数组各元素进行对应运算
        np.maximum(x,y) np.fmax()

        np.minimum(x,y) np.fmin()       元素级的最大值/最小值计算
        np.mod(x,y)                     元素级的模运算
        np.copysign(x,y)                将数组y中各元素值的符号赋值给数组x对应元素
        > < >= <= == !=                 算术比较，产生布尔型数组

"""
import numpy as np

# np.arange(n)        类似range()函数，返回ndarray类型，元素从0到n‐1
# np.ones(shape)      根据shape生成一个全1数组，shape是元组类型
# np.zeros(shape)     根据shape生成一个全0数组，shape是元组类型
# np.full(shape,val)  根据shape生成一个数组，每个元素值都是val
# np.eye(n)           创建一个正方的n*n单位矩阵，对角线为1，其余为0

# np_arange = np.arange(10)
# np_ones = np.ones((3,6))
# np_zeros = np.zeros((3,6))
# np_full = np.full((3,6),666)
# np_eye = np.eye(5)
# print(np_arange)
# print(np_ones)
# print(np_zeros)
# print(np_full)
# print(np_eye)

print("*"*32)
# 三维数组
a = np.ones((2,3,4), dtype=np.int32)
print(a)
# astype()方法一定会创建新的数组（原始数据的一个拷贝），即使两个类型一致
new_a = a.astype(np.float)
print(new_a)
# ndarray数组向列表的转换
ls = a.tolist()
print(ls)

print("一维数组")
a_index =np.array([9,8,7,6,5,4,3,2,1])
print(a_index[2])
print(a_index[1:4:2])

print("多维数组")
a_more = np.arange(24).reshape((2,3,4))
print(a_more)
print(a_more[1,2,3])
print(a_more[0,1,2])
print(a_more[-1,-2,-3])

print("多维数组的切片")
print(a_more[:,:,::2])

# NumPy一元函数实例
# 数组与标量之间的运算
# 数组与标量之间的运算作用于数组的每一个元素
print("a_more的平均值：\n{}".format(a_more.mean()))
print("a_more的平方：\n{}".format(np.square(a_more)))

# NumPy二元函数实例
b_more = np.sqrt(a_more)
print("b_more:{}".format(b_more))
print("a_more和b_more比较，取最大值:\n{}".format(np.maximum(a_more,b_more)))
print("a_more和b_more比较，取True or False:\n{}".format(a_more>b_more))