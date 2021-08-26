print("------ 遍历所有的键—值对 ----------")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

print("------ 遍历字典中的所有键 ----------")
for name in favorite_languages.keys():
    print(name.title())
# 遍历字典时，会默认遍历所有的键，因此，如果将上述代码中的for name in favorite_languages.keys():替换为for name in favorite_languages:，输出将不变。
print("................")
for name in favorite_languages:
    print(name.title())

print("------ 按顺序遍历字典中的所有键 ----------")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("------ 遍历字典中的所有值 ----------")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 为剔除重复项，可使用集合（set）
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
