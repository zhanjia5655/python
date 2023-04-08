numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # 输出: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出: [2, 4]

numbers = [5, 3, 1, 2, 4]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)  # 输出: [1, 2, 3, 4, 5]


