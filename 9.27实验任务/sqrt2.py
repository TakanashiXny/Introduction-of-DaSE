def sqrt1():
    g = 1
    h = 0.00001
    while abs(g ** 2 - 2) > 0.0001:
        g += h
    print(f"循环迭代, 逐步逼近得到的结果是: {g}")


def sqrt2():
    Min = 0
    Max = 2
    g = (Min + Max) / 2
    while abs(g ** 2 - 2) > 0.00000000001:
        if g ** 2 > 2:
            Max = g
        else:
            Min = g
        g = (Min + Max) / 2
    print(f"二分查找, 折半返回得到的结果是: {g}")


def sqrt3():
    c = 2
    g = c / 2
    while abs(g ** 2 - c) > 0.00000000001:
        g = (g + c / g) / 2
    print(f"曲线切线, 线性逼近得到的结果是: {g}")


if __name__ == '__main__':
    sqrt1()
    sqrt2()
    sqrt3()
