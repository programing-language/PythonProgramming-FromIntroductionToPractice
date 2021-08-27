# 有时候，提示可能超过一行，在这种情况下，可将提示存储在一个变量中，再将该变量传递给函数input()。
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
