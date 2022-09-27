import random
import math


# method 1: probability
def pi1():
    total = 100000
    Sum = 0
    for i in range(total):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 < 1:
            Sum += 1
    prob = Sum / total
    result = prob * 4
    print("%.10f" % result)


# method 2: Fourier
def pi2():
    Sum = 0
    for i in range(1, 1000):
        Sum += 1 / (i * i)
    result = math.sqrt(6 * Sum)
    print("%.10f" % result)


# method 3: arc-tan1
def pi3():
    Sum = 0
    for i in range(1000):
        Sum += (-1) ** i / (2 * i + 1)
    result = 4 * Sum
    print("%.10f" % result)


if __name__ == '__main__':
    pi1()
    pi2()
    pi3()
