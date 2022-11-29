import numpy as np
import matplotlib.pyplot as plt


with open(r'E:\学习\数据科学与工程导论\lab7\daily_KP_SUN_2020.csv', 'r', encoding='utf-8') as f1:
    s1 = f1.readlines()
    s2 = s1[3:]
    lst = []
    for i in range(len(s2)):
        s2[i] = s2[i].strip('\n').strip(",'C'").split(',')
        lst.append(s2[i])


total = np.zeros(9)
for k in lst:
    total[int(k[1]) - 1] += float(k[3])
month_total = np.array([31, 29, 31, 30, 31, 30, 31, 31, 30])
average = total / month_total


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = [i for i in range(1, 10)]
plt.subplot(211)
plt.bar(x, total, color='orange')
plt.title("每月总日照数")
plt.subplot(212)
plt.bar(x, average, color='red')
plt.title("每月平均日照数")
plt.subplots_adjust(hspace=1.0)
plt.show()
