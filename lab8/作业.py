import pymysql
import numpy as np


db = pymysql.connect(host="cdb-r2g8flnu.bj.tencentcdb.com", port=10209,
                     user="dase2020", password="dase2020", database="dase_intro_2020")
cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor,执行SQL语句都是通过游标对象实现


city_dic = {0: "北京", 1: "上海"}


sql = "SELECT * FROM bicycle_train LIMIT 17,5;"
cursor.execute(sql)
result = cursor.fetchall()
print(result)


sql = "SELECT MAX(wind),MIN(wind) FROM bicycle_train"
cursor.execute(sql)
result = cursor.fetchone()
print(f"取值范围为: {result[1]}~{result[0]}")


sql = "SELECT AVG(temp_air) FROM bicycle_train WHERE city=0 AND hour=10 AND weather=1 AND (wind=0 OR wind=1) AND y>=100"
cursor.execute(sql)
result = cursor.fetchone()
print(f"大气温度为{result[0]}")


sql = "SELECT temp_air FROM bicycle_train WHERE city=0 AND hour=10 AND weather=1 AND (wind=0 OR wind=1) AND y>=100"
cursor.execute(sql)
result = cursor.fetchall()
a = np.array(result)
lst = list(map(lambda x: int(x), a))
Var = np.var(lst)
print(f"大气温度方差为: {Var}")


sql = "SELECT city,SUM(y) FROM bicycle_train WHERE is_workday=1 AND weather=3 GROUP BY city ORDER BY SUM(y) DESC"
cursor.execute(sql)
result = cursor.fetchall()
print(f"{city_dic[result[0][0]]}工作日雨雪天单车租用量为{result[0][1]}, "
      f"{city_dic[result[1][0]]}工作日雨雪天单车租用量为{result[1][1]}")


sql = '''SELECT hour,AVG(y) FROM bicycle_train WHERE city=1 AND is_workday=1 AND temp_body<=10 GROUP BY hour HAVING hour 
         BETWEEN 17 AND 19 ORDER BY AVG(y)'''
cursor.execute(sql)
result = cursor.fetchall()
print(f"{result[0][0]}时{round(result[0][1])}辆, {result[1][0]}时{round(result[1][1])}辆, "
      f"{result[2][0]}时{round(result[2][1])}辆")

