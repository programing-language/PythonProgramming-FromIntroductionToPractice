#!/usr/bin/env python
# encoding: utf-8
'''
@author: chenjinxin
@file: cars.py
@time: 2021/8/5 下午4:32
@desc:
'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# sorted() 不影响原始数据
print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list:")
print(cars)

# reverse()：反转列表元素，改变原数据
cars.reverse()
print(cars)

# len()
print(len(cars))
