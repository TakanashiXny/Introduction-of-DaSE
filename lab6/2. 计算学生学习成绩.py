import numpy as np
import time


with open(r'E:\学习\数据科学与工程导论\lab6\stuGrade.csv', 'r', encoding='utf-8') as f:
    s = f.readline()
    lst = f.readlines()

stu = []
for i in lst:
    i = i.strip('\n')
    tmp = i.split(',')
    for j in range(len(tmp)):
        tmp[j] = int(tmp[j])
    stu.append(tmp)
Mean = np.mean(stu, axis=0)


ChineseMean = Mean[1]
MathMean = Mean[2]
EnglishMean = Mean[3]
print("语文学科的平均成绩为: %.2f" % ChineseMean)
print("数学学科的平均成绩为: %.2f" % MathMean)
print("英语学科的平均成绩为: %.2f" % EnglishMean)


my_id = '10215501438'
name = '韩弈文'

with open(r'E:\学习\数据科学与工程导论\lab6\作业.txt', 'w', encoding='utf-8') as f2:
    info1 = my_id + ' ' + name + '\n'
    f2.write(info1)
    info2 = '{:.2f}, {:.2f}, {:.2f}'.format(ChineseMean, MathMean, EnglishMean) + '\n'
    f2.write(info2)
    info3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
    f2.write(info3)
    time.sleep(2)
    info4 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f2.write(info4)


print("over!")

