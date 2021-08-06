#!/usr/bin/env python
# encoding: utf-8
'''
@author: chenjinxin
@file: cars.py
@time: 2021/8/6 下午5:40
@desc:
'''
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
