lst = [1, 2, 3, 4, 5]
size = len(lst)

# 使用for循环
print("用for循环得到的结果是: ")
for i in range(len(lst) - 1, -1, -1):
    print(lst[i], end=' ')
print()

# 使用while循环
print("用while循环得到的结果是: ")
index = len(lst) - 1
while index >= 0:
    print(lst[index], end=' ')
    index -= 1
print()

# 使用数组切片
print("使用数组切片得到的结果是: ")
lst2 = lst[::-1]
for i in lst2:
    print(i, end=' ')

