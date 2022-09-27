def longest(string: str) -> int:
    Max = 0
    size = len(string)
    index = 0
    while index < size:
        letter = string[index]
        index2 = index + 1
        # 遍历到最后一个满足要求的字符的后一个
        while index2 < size and letter == string[index2]:
            index2 += 1
        length = index2 - index
        if length > Max:
            Max = length
        index = index2
    return Max


if __name__ == '__main__':
    s = input("请输入一个字符串: ")
    result = longest(s)
    if result >= 2:
        print("包含两个或两个以上连续出现的相同字符组成的字符串")
    else:
        print("不包含两个或两个以上连续出现的相同字符组成的字符串")
    print(f"最长连续出现的字符长度是: {result}")
