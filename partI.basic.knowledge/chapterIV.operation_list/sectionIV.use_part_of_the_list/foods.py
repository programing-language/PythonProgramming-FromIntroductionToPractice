#!/usr/bin/env python
# encoding: utf-8
'''
@author: chenjinxin
@file: foods.py
@time: 2021/8/6 下午4:10
@desc:
'''
my_foods = ['pizza', 'falafel', 'carrot cake']

# 值传递
friend_foods = my_foods[:]

# 引用传递
my_foods2 = my_foods
my_foods2.append('cannoli')

friend_foods.append('ice cream')

print(my_foods)
print(my_foods2)
print(friend_foods)
