file_path = '../docs/pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    # rstrip()删除（剥除）字符串末尾的空白。
    print(contents.rstrip())
