import random


def partition(lst: list, left: int, right: int) -> int:
    key = lst[right]
    i = left - 1
    for j in range(left, right):
        if lst[j] <= key:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[right], lst[i+1] = lst[i+1], lst[right]
    return i+1


def randomized_partition(lst: list, left: int, right: int) -> int:
    i = random.randint(left, right)
    lst[i], lst[right] = lst[right], lst[i]
    return partition(lst, left, right)


def randomized_quicksort(lst: list, left: int, right: int) -> None:
    if left < right:
        q = randomized_partition(lst, left, right)
        randomized_quicksort(lst, left, q-1)
        randomized_quicksort(lst, q+1, right)


if __name__ == '__main__':
    s = input("请输入一列要排序的数字: ").split()
    num = list(map(lambda x: int(x), s))
    randomized_quicksort(num, 0, len(num)-1)
    print(num)

