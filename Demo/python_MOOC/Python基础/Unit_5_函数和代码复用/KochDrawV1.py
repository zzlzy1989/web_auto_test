# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/24 16:30
# @File     : KochDrawV1.py
# @Software : web_auto_test


# 科赫曲线绘制源代码

import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
           turtle.left(angle)
           koch(size/3, n-1)
def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600,3)     # 0阶科赫曲线长度，阶数
    turtle.hideturtle()
main()