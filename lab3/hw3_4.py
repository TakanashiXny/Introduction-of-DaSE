import random
import math


def fun(variable):
    return variable ** 2 + 4 * variable * math.sin(variable)


if __name__ == '__main__':
    cnt = 0
    total = 10000
    high = 25
    left = 2
    right = 3
    for i in range(cnt, total + 1):
        x = random.uniform(left, right)
        y = random.uniform(0, high)
        if y <= fun(x):
            cnt += 1
    result = cnt / total * 25
    print("这个定积分的值是: %f" % result)
