def bubble_sort(lst: list) -> list:
    size = len(lst)
    for i in range(1, size):
        for j in range(size-i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == '__main__':
    s = input("请输入一列要排序的数字: ")
    num = s.split()
    num = list(map(lambda x: int(x), num))
    result = bubble_sort(num)
    print(result)
