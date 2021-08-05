#!/usr/bin/env python
# encoding: utf-8
'''
@author: chenjinxin
@file: motorcycles.py
@time: 2021/8/5 下午4:06
@desc:
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modify
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# add
motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# del
del motorcycles[0]
print(motorcycles)
# pop默认弹出最后一个
pop_motorcycle = motorcycles.pop()
print(motorcycles)
print(pop_motorcycle)
first_pop = motorcycles.pop(0)
print(motorcycles)
print(first_pop)
# 根据值删除元素: remove()只删除第一个指定的值。
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")
