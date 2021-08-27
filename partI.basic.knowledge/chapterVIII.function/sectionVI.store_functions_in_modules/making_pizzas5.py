# 导入模块中的所有函数
# from module_name import *
"""
由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。
然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法：如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：
Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。
"""


from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
