# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/24 16:11
# @File     : CalPiV2.py
# @Software : web_auto_test


from random import random
from time import perf_counter

# 程序计时函数perf_counter()
'''
    返回一个CPU级别的精确时间计数值，单位为秒。
    代码如下：
        import time
        start=time.perf_counter()
        print("start:",start)
        end=time.perf_counter()
        print("\nend:",end)
        duration=end-start
        print("\nThe duration is:",duration)
    此代码为获得两次指令之间的持续时间！
'''

DARTS = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("圆周率值是: {}".format(pi))
print("运行时间是: {:.5f}s".format(perf_counter() - start))


import time
start = time.perf_counter()
print("start:", start)
time.sleep(1)
end = time.perf_counter()
print("\nend:", end)
duration = end - start
print("\nThe duration is:{:.5f}s".format(duration))