# coin = [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2]
# total = 0
# result = -1
# for i in coin:
#     total += i
# left = 0
# right = len(coin)-1
# while not left == right:
#     cnt = right-left+1
#     if cnt % 2 == 0:
#         LeftSum = 0
#         for i in coin[left:(left+right)//2+1]:
#             LeftSum += i
#         RightSum = total - LeftSum
#         if LeftSum > RightSum:
#             left = (left+right)/2+1
#             total = RightSum
#             continue
#         else:
#             right = (left+right)//2
#             total = LeftSum
#             continue
#     else:
#         LeftSum = 0
#         middle = (left+right)//2
#         for i in coin[left:middle]:
#             LeftSum += i
#         RightSum = total-LeftSum-coin[middle]
#         if LeftSum == RightSum:
#             result = middle
#             break
#         elif LeftSum < RightSum:
#             right = middle-1
#             total = LeftSum
#             continue
#         else:
#             left = middle+1
#             total = RightSum
#             continue
# if left == right:
#     result = left
# print("假币的序号是%d" % result)

def divide_conquer(lst, left, right):
    if left == right:
        return left
    cnt = right - left + 1
    if cnt % 2 == 0:
        mid = (left + right) // 2
        LeftSum = 0
        RightSum = 0
        for i in lst[left:mid + 1]:
            LeftSum += i
        for i in lst[mid + 1:right + 1]:
            RightSum += i
        if LeftSum < RightSum:
            return divide_conquer(lst, left, mid)
        else:
            return divide_conquer(lst, mid + 1, right)
    else:
        mid = (left + right) // 2
        LeftSum = 0
        RightSum = 0
        for i in lst[left:mid]:
            LeftSum += i
        for i in lst[mid + 1:right + 1]:
            RightSum += i
        if LeftSum == RightSum:
            return mid
        elif LeftSum < RightSum:
            return divide_conquer(lst, left, mid - 1)
        else:
            return divide_conquer(lst, mid + 1, right)


if __name__ == '__main__':
    coin = [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2]
    result = divide_conquer(coin, 0, len(coin)-1)
    print("假币的序号是%d" % result)
