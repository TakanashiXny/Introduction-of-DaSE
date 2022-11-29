def d_to_b(num: int) -> str:
    result = ""
    cnt = 0
    while num > 0:
        quotient = num // 2
        remainder = num % 2
        num = quotient
        result = str(remainder) + result
        cnt += 1
    plus = "0" * (8 - cnt)
    result = plus + result
    return result


if __name__ == '__main__':
    ipv4 = "203.179.25.37"
    lst = ipv4.split(".")
    ans = ""
    for i in lst:
        ans += d_to_b(int(i))
    print(ans)
