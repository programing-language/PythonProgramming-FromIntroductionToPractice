#!/usr/bin/env python
# encoding: utf-8
'''
@author: chenjinxin
@file: dimensions.py
@time: 2021/8/6 下午5:11
@desc:
'''
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。
dimensions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)

