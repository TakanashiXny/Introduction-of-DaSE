import pymysql
import csv
import pandas as pd
import matplotlib.pyplot as plt

db = pymysql.connect(host="cdb-r2g8flnu.bj.tencentcdb.com", port=10209,
                     user="dase2020", password="dase2020", database="dase_intro_2020")
cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor,执行SQL语句都是通过游标对象实现

sql = "SELECT * FROM SH_Grade"
cursor.execute(sql)
result = cursor.fetchall()
lst = []
for i in result:
    lst.append(list(i))
print(lst)
for i in range(len(lst)):
    lst[i].insert(2, lst[i][1][0])

header = ['id', 'StuId', 'Class', 'Sex', 'CHI611', 'MATH611', 'ENG611', 'CHI612', 'MATH612', 'ENG612',
          'CHI621', 'MATH621', 'ENG621', 'CHI622', 'MATH622', 'ENG622',
          'CHI711', 'MATH711', 'ENG711', 'CHI712', 'MATH712', 'ENG712',
          'CHI721', 'MATH721', 'ENG721', 'CHI722', 'MATH722', 'ENG722',
          'CHI811', 'MATH811', 'ENG811', 'PHY811', 'CHI812', 'MATH812', 'ENG812', 'PHY812',
          'CHI821', 'MATH821', 'ENG821', 'PHY821', 'CHI822', 'MATH822', 'ENG822', 'PHY822',
          'CHI911', 'MATH911', 'ENG911', 'PHY911', 'CHE911', 'CHI912', 'MATH912', 'ENG912', 'PHY912', 'CHE912',
          'CHI921', 'MATH921', 'ENG921', 'PHY921', 'CHE921']
with open(r"E:\学习\数据科学与工程导论\lab9\SH_Grade.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for stu in lst:
        writer.writerow(stu)

print("over!")

stu_data = pd.read_csv(r"E:\学习\数据科学与工程导论\lab9\SH_Grade.csv")
print(f'处理前{stu_data.shape[0]}条')
stu_data_norepeat = stu_data.drop_duplicates(subset=['StuId'])
print(f'去重处理后{stu_data_norepeat.shape[0]}条')

stu_data_complete = stu_data_norepeat.dropna(thresh=stu_data.shape[1] - 12)
print(f'剔除大于等于12个字段为空的数据行后{stu_data_complete.shape[0]}条')

stu_data_fill = stu_data_complete.copy()
stu_data_fill['Sex'] = stu_data_fill['Sex'].fillna(method='ffill')
for i in header[4:]:
    stu_data_fill[i] = stu_data_fill[i].fillna(stu_data_fill[i].median())
print(stu_data_fill)

stu_data_trans = stu_data_fill.copy()
for i in header[4:]:
    if 100 < stu_data_trans[i].max() <= 120:
        stu_data_trans[i] = stu_data_trans[i].apply(lambda x: x / 120 * 100)
    elif stu_data_trans[i].max() > 120:
        stu_data_trans[i] = stu_data_trans[i].apply(lambda x: x / 150 * 100)
    elif i[0:4] == "PHY9":
        stu_data_trans[i] = stu_data_trans[i].apply(lambda x: x / 90 * 100)
    elif i[0:3] == "CHE":
        stu_data_trans[i] = stu_data_trans[i].apply(lambda x: x / 60 * 100)
print(stu_data_trans)


male = stu_data_trans.loc[stu_data_trans['Sex'] == 'M'].groupby('Class')['Sex'].count()
print(male)
female = stu_data_trans.loc[stu_data_trans['Sex'] == 'F'].groupby('Class')['Sex'].count()
print(female)
plt.bar(['A', 'B', 'C', 'D', 'E', 'F', 'G'], male.values, label='male')
plt.bar(['A', 'B', 'C', 'D', 'E', 'F', 'G'], female, bottom=male.values, label='female')
plt.legend()
plt.show()


Chinese = []
for i in header:
    if i[0:3] == 'CHI':
        Chinese.append(i)
Chinese_Score = stu_data_trans[Chinese]
a13 = Chinese_Score.loc[stu_data_trans['StuId'] == 'A13']
x = Chinese.copy()
y = a13.values[0]
plt.plot(x, y, color='orange')
a15 = Chinese_Score.loc[stu_data_trans['StuId'] == 'A15']
x = Chinese.copy()
y = a15.values[0]
plt.plot(x, y, color='blue')
plt.xticks([Chinese[i] for i in range(0, len(Chinese), 3)])
plt.legend(['A13', 'A15'])
plt.show()


lst = ['StuId', 'Class', 'ENG721', 'CHI721']
fail = stu_data_trans.loc[(stu_data_trans['ENG721'] < 60) | (stu_data_trans['CHI721'] < 60)][lst]
print(fail)


lst2 = ['CHI622', 'MATH622', 'ENG622']
Mean = stu_data_trans.loc[(stu_data_trans['Class'] == 'A') | (stu_data_trans['Class'] == 'C')].groupby("Class")[lst2].mean()
print(Mean)
Var = stu_data_trans.loc[(stu_data_trans['Class'] == 'A') | (stu_data_trans['Class'] == 'C')].groupby("Class")[lst2].var()
print(Var)
# A班语文虽然均分较高，但是成绩差异较大
# 数学成绩略高于C班，同时学生差异远小于C班
# A班英语略落后于C班，但是学生差异略小


fail.to_csv(r'E:\学习\数据科学与工程导论\lab9\task8.csv', index=0)
