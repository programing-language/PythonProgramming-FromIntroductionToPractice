# == != < <= > >=
answer = 17

if answer != 42:
    print("That is not the corect answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)


# and or
print("-----------and--------------")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 21
print(age_0 >= 21 and age_1 >= 21)
print((age_0 >= 21) and (age_1 >= 21))

print("-----------or---------------")
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

print("-----------in---------------")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

print("--------not in---------------")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
