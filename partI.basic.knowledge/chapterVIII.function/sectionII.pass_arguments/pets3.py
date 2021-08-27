# 默认值
""" 注意　使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。这让Python依然能够正确地解读位置实参。 """


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('harry')
describe_pet(pet_name='harry')
describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry')
