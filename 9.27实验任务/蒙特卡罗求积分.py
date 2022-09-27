import random

total = 10000
Sum = 0
Left = 0
Right = 1
Min = 0
Max = 2
S = (Right-Left)*(Max-Min)
for i in range(0, total):
    x = random.uniform(Left, Right)
    y = random.uniform(Min, Max)
    if y <= x ** 3 + x ** 2:
        Sum += 1
prob = Sum / total
result = prob * S
print(f"这个定积分的结果是: {result}")
