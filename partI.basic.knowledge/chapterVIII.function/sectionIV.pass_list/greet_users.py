# 传递列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


username_list = ['hannah', 'ty', 'margot']
greet_users(username_list)
