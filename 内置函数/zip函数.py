# 将两个列表打包成一个元组序列
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = zip(list1, list2)
print(list(result))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# 将三个列表打包成一个元组序列
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]
result = zip(list1, list2, list3)
print(list(result))  # [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

# 将两个字符串打包成一个字符序列
str1 = 'abc'
str2 = '123'
result = zip(str1, str2)
print(list(result))  # [('a', '1'), ('b', '2'), ('c', '3')]

# 使用for循环逐个访问zip对象中的元素
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item in zip(list1, list2):
    print(item)  # (1, 'a') (2, 'b') (3, 'c')
