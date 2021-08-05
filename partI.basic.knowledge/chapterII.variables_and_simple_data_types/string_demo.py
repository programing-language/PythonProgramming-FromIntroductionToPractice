#!/usr/bin/env python
# encoding: utf-8
'''
@author: chenjinxin
@file: string_demo.py
@time: 2021/8/5 上午11:03
@desc:
'''
# title()：单词的首字母大写，其余字母小写
name = "ada lovelace"
print(name.title())

name = "aDa loveLace"
print(name.title())

# upper(): 所有字母大写
print(name.upper())
# lower(): 所有字母小写
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + ' ' + last_name
print(full_name)
message = "Hello, " + full_name.title() + "!"
print(message)

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# rstrip(): 删除字符串末尾的空白
# lstrip(): 删除字符串开头的空白
# strip(): 删除字符串两端的空白
favorite_language = " python "
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
