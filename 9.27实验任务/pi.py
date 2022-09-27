import random
import math


# method 1: 无穷级数
def pi1():
    cnt = 0
    Sum = 0
    while abs(Sum - math.pi ** 2 / 6) > 0.0000000001:
        cnt += 1
        Sum += 1 / (cnt ** 2)
    result = math.sqrt(6 * Sum)
    print("%.10f" % result)
    print(f"进行了{cnt}次")


# method 2: arc-tan1
def pi2():
    Sum = 0
    cnt = 0
    while abs(Sum - math.pi / 4) > 0.000000001:
        Sum += (-1) ** cnt / (2 * cnt + 1)
        cnt += 1
    result = Sum * 4
    print("%.10f" % result)
    print(f"进行了{cnt}次")


# method 3: 蒙特卡罗概率
def pi3():
    Sum = 0
    total = 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        Sum = 1
    while abs(Sum / total * 4 - math.pi) > 0.000000001:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 < 1:
            Sum += 1
        total += 1
    result = Sum / total * 4
    print("%.10f" % result)
    print(f"进行了{total}次")


if __name__ == '__main__':
    pi1()
    pi2()
    pi3()
