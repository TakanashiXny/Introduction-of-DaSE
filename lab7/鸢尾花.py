import matplotlib.pyplot as plt


with open(r'E:\学习\数据科学与工程导论\lab7\iris.csv', 'r', encoding='utf-8') as f2:
    s1 = f2.readlines()
    lst = s1[1:]


for i in range(len(lst)):
    lst[i] = lst[i].strip('\n').split(',')


Sepal_Length = []
Sepal_Width = []
Petal_Length = []
Petal_Width = []
for i in lst:
    Sepal_Length.append(float(i[0]))
    Sepal_Width.append(float(i[1]))
    Petal_Length.append(float(i[2]))
    Petal_Width.append(float(i[3]))


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(231)
plt.scatter(Sepal_Length[1:52], Sepal_Width[1:52], s=3, color="blue")
plt.scatter(Sepal_Length[52:102], Sepal_Width[52:102], s=3, color="green")
plt.scatter(Sepal_Length[102:152], Sepal_Width[102:152], s=3, color="red")
plt.title("花萼长度与花萼宽度")

plt.subplot(232)
plt.scatter(Sepal_Length[1:52], Petal_Length[1:52], s=3, color="blue")
plt.scatter(Sepal_Length[52:102], Petal_Length[52:102], s=3, color="green")
plt.scatter(Sepal_Length[102:152], Petal_Length[102:152], s=3, color="red")
plt.title("花萼长度与花瓣长度")

plt.subplot(233)
plt.scatter(Sepal_Length[1:52], Petal_Width[1:52], s=3, color="blue")
plt.scatter(Sepal_Length[52:102], Petal_Width[52:102], s=3, color="green")
plt.scatter(Sepal_Length[102:152], Petal_Width[102:152], s=3, color="red")
plt.title("花萼长度与花瓣宽度")

plt.subplot(234)
plt.scatter(Sepal_Width[1:52], Petal_Length[1:52], s=3, color="blue")
plt.scatter(Sepal_Width[52:102], Petal_Length[52:102], s=3, color="green")
plt.scatter(Sepal_Width[102:152], Petal_Length[102:152], s=3, color="red")
plt.title("花萼宽度与花瓣长度")

plt.subplot(235)
plt.scatter(Sepal_Width[1:52], Petal_Width[1:52], s=3, color="blue")
plt.scatter(Sepal_Width[52:102], Petal_Width[52:102], s=3, color="green")
plt.scatter(Sepal_Width[102:152], Petal_Width[102:152], s=3, color="red")
plt.title("花萼长度与花瓣宽度")

plt.subplot(236)
plt.scatter(Petal_Length[1:52], Petal_Width[1:52], s=3, color="blue")
plt.scatter(Petal_Length[52:102], Petal_Width[52:102], s=3, color="green")
plt.scatter(Petal_Length[102:152], Petal_Width[102:152], s=3, color="red")
plt.title("花瓣长度与花瓣宽度")

plt.subplots_adjust(hspace=1.0)
plt.show()
