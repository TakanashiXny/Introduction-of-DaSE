lst = [2 * i + 1 for i in range(0, 50)]  # 生成1-100以内的奇数
print("1到100中所有奇数为: ")
for i in lst:
    print(i, end=" ")
print()
result = 1
for i in range(0, 25):
    result *= lst[i]
print("这些50以内奇数的乘积为: %d" % result)
