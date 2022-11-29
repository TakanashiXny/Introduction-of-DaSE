def factorial(num):
    if num == 1 or num == 0:
        return 1
    elif num > 1:
        return num * factorial(num - 1)


if __name__ == '__main__':
    n = int(input('请输入一个自然数: '))
    result = factorial(n)
    print("这个数的阶乘是%d" % result)
