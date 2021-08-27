from collections import OrderedDict

# OrderedDict实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序。
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")
