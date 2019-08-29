# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/29 14:42
# @File     : 期末考试-02.py
# @Software : web_auto_test
"""

文件关键行数
描述
关键行指一个文件中包含的不重复行。关键行数指一个文件中包含的不重复行的数量。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

统计附件文件中与关键行的数量。

"""
dict = {}
with open('latex.log', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        rline=line
        dict[rline] = dict.get(rline,0)+1

print('{}'.format(len(dict)))