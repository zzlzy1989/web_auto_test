# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time     : 2019/6/20 0020 00:34
# # @Author   : 蓝天下的风
# # @File     : 总结+自动化.py
# # Project   : web_auto_test
# # @Software : PyCharm
#
#
#
# html+dom
# 元素定位 - 8  xpath- 多种
# 元素操作：4大基本：send_keys,click,text,get_attribute
# 等待 - 3种 sleep-助攻   显性等待-主攻   隐性等待-幕后/佯攻
# 3种切换 - switch_to     window , iframe ， alert  - 先找到，再切换。
# 下拉列表-Select  鼠标操作 - ActionChains  按键操作 - Keys
# js助攻 - 日历 / 修改属性 /滚动条
# 上传 - windows - autoit/pywin32 -windows     --mac sikuli
#
# 画个思维导图。
#
# 项目实战  # 前程贷项目 - web自动化？ - 一份大概的执行计划。
# 为什么要做web自动化测试？接口自动化。
# 自动化的目的：前置、步骤、期望结果() - 1点。写一份脚本 - 运行N遍 - 测试N次
# 1 - 2个测试 - 10个功能 - 2天 - 上线频率：2周1次
# 2 - 2个测试 - 100个功能 - 10天 - 上线频率：2周1次 - 所有功能都得测。
# 50个功能 - 重复测试了50遍 - 同样的功能点点点。  -- 枯燥/重复/烦
# -- 重复工作，没有提升。
# --每次点的时候，不会覆盖所有的细节功能。
# -- 上线，历史功能出问题。
#
# 尽量避免上线出问题  -- 客户反馈过的问题，适当加入自动化当中。
# 解放双手、解放时间  -- 提高一个测试反馈效率。
# 每次回归的功能都保持一致 -- 自动化的用例是什么，每次都运行的什么。
#
# 项目周期比较长 - 历史功能(稳定)
#
# 在开发后台接口的阶段，同步做接口自动化测试   -- 70% - 100%  (单接口 + 流程场景)
#    -  团队的质量意识/单元测试/测试能力高/沟通要及时
#  -- web自动化 - 最接近用户操作。-- 20%  -- 主流程 + 易实现的异常用例
#
#
# 用工具和框架的区别？
#
# # 项目实战  # 前程贷项目 - web自动化？ - 一份大概的执行计划。
# 1、了解被测对象 - 业务需求。
# 2、功能模块？1000功能用例 - 5大模块。  上线bug率最高的模块 - 核心模块 - 稳定的
# 3、测试用例？500个功能用例 - 50-100个左右 主流程业务 + 易实现的异常用例。
# 其它测试人员
# 实现100个功能用例 - 自动化 -
# 4、框架选型  -  自己写 - python+selenium+..... 2周
# 整体的测试水平。1个人 - 由你最熟悉的技能来实现。  团队 - 工具(规范)
# 框架 - 规定哪些层级里放什么,规定编写规则-文件命名/定位的规则/注释要求等，准备示范的例子。
#   - 结构设计+规范。--管理、灵活扩展、维护工作量少
#   - 尽早定期评审团队成员脚本  - 发现问题，解决问题，定规则。
# 标准就是：较好的可读性、注释量要有以免回头看不懂写的啥。
#
# 5、实现脚本 - PO模式
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
