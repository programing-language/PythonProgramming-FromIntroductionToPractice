#!/usr/bin/env python
# encoding: utf-8
'''
@author: chenjinxin
@file: numbers.py
@time: 2021/8/6 下午3:20
@desc:
'''
# range(n, m): [n, m)
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

# 设置步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 创建一个列表，其中包含前10个整数（即1~10）的平方
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
