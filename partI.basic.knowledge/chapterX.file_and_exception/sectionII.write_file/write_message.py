# 打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'）。
# 如果你省略了模式实参，Python将以默认的只读模式打开文件。

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming")
