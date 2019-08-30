# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/8/24 16:38
# @File     : CalThreeKingdomsV1.py
# @Software : web_auto_test

import jieba

# 《三国演义》人物出场统计（上）（含《三国演义》原文文本）

txt = open("threekingdoms.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))