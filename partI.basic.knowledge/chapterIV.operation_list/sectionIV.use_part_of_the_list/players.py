#!/usr/bin/env python
# encoding: utf-8
'''
@author: chenjinxin
@file: players.py
@time: 2021/8/6 下午4:01
@desc:
'''
# 切片: [n:m] -> [n, m)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 不指定第一个索引，则自动从列表开头开始
print(players[:3])

# 不指定第二个索引，则自动截止到列表结尾
print(players[3:])

# 遍历切片: 输出名单上的最后三名队员
for player in players[-3:]:
    print(player)
