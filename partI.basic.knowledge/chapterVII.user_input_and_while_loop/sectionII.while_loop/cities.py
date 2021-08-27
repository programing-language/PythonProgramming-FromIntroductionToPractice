# 使用break退出循环
# 在任何Python循环中都可使用break语句。例如，可使用break语句来退出遍历列表或字典的for循环。
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
