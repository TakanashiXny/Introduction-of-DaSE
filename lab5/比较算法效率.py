import random
import time


def bubble_sort(lst: list) -> list:
    size = len(lst)
    for i in range(1, size):
        for j in range(size-i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def partition(lst: list, left: int, right: int) -> int:
    key = lst[right]
    i2 = left - 1
    for j in range(left, right):
        if lst[j] <= key:
            i2 += 1
            lst[i2], lst[j] = lst[j], lst[i2]
    lst[right], lst[i2+1] = lst[i2+1], lst[right]
    return i2+1


def randomized_partition(lst: list, left: int, right: int) -> int:
    i3 = random.randint(left, right)
    lst[i3], lst[right] = lst[right], lst[i3]
    return partition(lst, left, right)


def randomized_quicksort(lst: list, left: int, right: int) -> None:
    if left < right:
        q = randomized_partition(lst, left, right)
        randomized_quicksort(lst, left, q-1)
        randomized_quicksort(lst, q+1, right)


if __name__ == '__main__':
    times = 10000
    arr1 = []
    for i in range(times):
        arr1.append(random.random())
    arr2 = arr1.copy()
    bubble_start = time.perf_counter()
    arr1 = bubble_sort(arr1)
    bubble_end = time.perf_counter()
    print("冒泡排序时间消耗为: %.4fs" % (bubble_end-bubble_start))

    quick_start = time.perf_counter()
    randomized_quicksort(arr2, 0, times-1)
    quick_end = time.perf_counter()
    print("随机化的快速排序时间消耗为: %.4fs" % (quick_end-quick_start))
