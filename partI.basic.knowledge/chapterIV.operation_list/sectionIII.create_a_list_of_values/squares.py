#!/usr/bin/env python
# encoding: utf-8
'''
@author: chenjinxin
@file: squares.py
@time: 2021/8/6 下午3:32
@desc:
'''
# 前面介绍的生成列表squares的方式包含三四行代码，而列表解析让你只需编写一行代码就能生成这样的列表。
# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。
squares = [value ** 2 for value in range(1, 11)]
print(squares)
