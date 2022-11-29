from concurrent.futures import ThreadPoolExecutor


def fun1(name):
    for i in range(50):
        print(name, i)


def fun2(name):
    for i in range(50):
        print(name, i)


if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        for i in range(10):
            t.submit(fun1, f'hyw{i}')
            t.submit(fun2, f'lre{i}')
    print('over!!!')
