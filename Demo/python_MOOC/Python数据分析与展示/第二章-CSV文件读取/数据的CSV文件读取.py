# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/31 16:16
# @File     : 数据的CSV文件读取.py
# @Software : web_auto_test

'''
CSV文件
    CSV (Comma‐Separated Value, 逗号分隔值)
    CSV是一种常见的文件格式，用来存储批量数据

    np.savetxt(frame, array, fmt='%.18e', delimiter=None)
    • frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文
    • array : 存入文件的数组
    • fmt : 写入文件的格式，例如：%d %.2f %.18e
    • delimiter : 分割字符串，默认是任何空格

    np.loadtxt(frame, dtype=np.float, delimiter=None， unpack=False)
    • frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文件
    • dtype : 数据类型，可选
    • delimiter : 分割字符串，默认是任何空格
    • unpack : 如果True，读入属性将分别写入不同变量

    CSV只能有效存储一维和二维数组
    np.savetxt() np.loadtxt()只能有效存取一维和二维数组

任意纬度的读取
    a.tofile(frame, sep='', format='%s')
    • frame : 文件、字符串
    • sep : 数据分割字符串，如果是空串，写入文件为二进制
    • format : 写入数据的格式

    np.fromfile(frame, dtype=float, count=‐1, sep='')
    • frame : 文件、字符串
    • dtype : 读取的数据类型
    • count : 读入元素个数，‐1表示读入整个文件
    • sep : 数据分割字符串，如果是空串，写入文件为二进制

    该方法需要读取时知道存入文件时数组的维度和元素类型
    a.tofile()和np.fromfile()需要配合使用
    可以通过元数据文件来存储额外信息
    np.save(fname, array) 或 np.savez(fname, array)
    • fname : 文件名，以.npy为扩展名，压缩扩展名为.np
    • array : 数组变量
    np.load(fname) • fname : 文件名，以.npy为扩展名，压缩扩展名为.npz



'''

import numpy as np
"""
    # CSV只能有效存储一维和二维数组
    # np.savetxt() np.loadtxt()只能有效存取一维和二维数组
"""
a = np.arange(100).reshape(5,20)
np.savetxt('a.csv', a, fmt='%d', delimiter=',')

b = np.loadtxt('a.csv',dtype=np.int,delimiter=',')
print(b)



"""
# 多维数据的存储
    a.tofile(frame, sep='', format='%s')
    • frame : 文件、字符串
    • sep : 数据分割字符串，如果是空串，写入文件为二进制
    • format : 写入数据的格式
    np.fromfile(frame, dtype=float, count=‐1, sep='')
    • frame : 文件、字符串
    • dtype : 读取的数据类型
    • count : 读入元素个数，‐1表示读入整个文件
    • sep : 数据分割字符串，如果是空串，写入文件为二进制
    
    该方法需要读取时知道存入文件时数组的维度和元素类型
    a.tofile()和np.fromfile()需要配合使用
    可以通过元数据文件来存储额外信息
    np.save(fname, array) 或 np.savez(fname, array) 
    • fname : 文件名，以.npy为扩展名，压缩扩展名为.np
    • array : 数组变量
    np.load(fname) • fname : 文件名，以.npy为扩展名，压缩扩展名为.npz

"""
a_more = np.arange(100).reshape(5,10,2)
a_more.tofile("b.dat",sep = ",",format ="%d")
# print(a_more)
# c_more = np.fromfile("",dtype=float,count=-1,sep="")
# print(c_more)

a = np.arange(100).reshape(5,10,2)
np.save("a.npy",a)
b = np.load("a.npy")
print("b:\n{}".format(b))

