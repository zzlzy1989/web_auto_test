# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/31 17:22
# @File     : 图像的手绘效果.py
# @Software : web_auto_test

'''
图像一般使用RGB色彩模式，即每个像素点的颜色由红(R)、绿(G)、蓝(B)组成
RGB三个颜色通道的变化和叠加得到各种颜色，其中
• R 红色，取值范围，0‐255
• G 绿色，取值范围，0‐255
• B 蓝色，取值范围，0‐255
RGB形成的颜色包括了人类视力所能感知的所有颜色。

PIL， Python Image Library
PIL库是一个具有强大图像处理能力的第三方库
在命令行下的安装方法： pip install pillow
from PIL import Image
Image是PIL库中代表一个图像的类（对象）

'''
from PIL import Image
import numpy as np

a = np.array(Image.open("panda\panda.jpg"))
# print(a.shape,a.dtype)
b = [255,255,255]-a
im = Image.fromarray(b.astype("uint8"))
im.save("panda\panda2.jpg")

a = np.array(Image.open("panda\panda.jpg").convert('L'))
# print(a.shape,a.dtype)
b = 255 - a
im = Image.fromarray(b.astype("uint8"))
im.save("panda\panda3.jpg")

a = np.array(Image.open("panda\panda.jpg").convert('L'))
# print(a.shape,a.dtype)
b = (100/255)*a + 150   # 区间变换
im = Image.fromarray(b.astype("uint8"))
im.save("panda\panda4.jpg")

a = np.array(Image.open("panda\panda.jpg").convert('L'))
# print(a.shape,a.dtype)
b = 255* (a/255)**2  ## 像素平方
im = Image.fromarray(b.astype("uint8"))
im.save("panda\panda5.jpg")

"""
手绘效果的几个特征：
• 黑白灰色
• 边界线条较重
• 相同或相近色彩趋于白色
• 略有光源效果
"""
