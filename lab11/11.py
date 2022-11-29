import pymysql
import pandas as pd
import csv
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
scale = MinMaxScaler()


def change_hour(time):
    if 6 <= time <= 18:
        return 1
    else:
        return 0

db = pymysql.connect(host="cdb-r2g8flnu.bj.tencentcdb.com", port=10209,
                     user="dase2020", password="dase2020", database="dase_intro_2020")
cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor,执行SQL语句都是通过游标对象实现


sql = "SELECT * FROM bicycle_train"
cursor.execute(sql)
result = cursor.fetchall()


lst = []
for i in result:
    lst.append(list(i))


header = ["id", "city", "hour", "is_workday", "weather", "temp_1", "temp_2", "wind", "y"]


with open(r"E:\学习\数据科学与工程导论\lab11\bike.csv", "w", encoding='utf-8', newline="") as f1:
    writer = csv.writer(f1)
    writer.writerow(header)
    for i in lst:
        writer.writerow(i)


data = pd.read_csv(r"E:\学习\数据科学与工程导论\lab11\bike.csv")


data_1 = data.drop('id', axis=1)


data_2 = data_1.loc[data_1['city'] == 1]
data_2 = data_2.drop('city', axis=1)


data_2.loc[data_2['hour'] >= 19, 'hour'] = 0
data_2.loc[data_2['hour'] <= 5, 'hour'] = 0
data_2.loc[data_2['hour'] != 0, 'hour'] = 1


y = data_2['y'].to_numpy()
y = y.reshape(len(y), 1)
data_2 = data_2.drop('y', axis=1)


data_2 = data_2.to_numpy()


x_train, x_test, y_train, y_test = train_test_split(data_2, y, test_size=0.2)
x_train = scale.fit_transform(x_train)
x_test = scale.fit_transform(x_test)
y_train = scale.fit_transform(y_train)
y_test = scale.fit_transform(y_test)


model = LinearRegression()
model.fit(x_train, y_train)


y_predict = model.predict(x_test)


print(mean_squared_error(y_test, y_predict)**0.5)
