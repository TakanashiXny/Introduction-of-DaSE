import pymysql

db = pymysql.connect(host="cdb-r2g8flnu.bj.tencentcdb.com", port=10209,
                     user="dase2020", password="dase2020", database="dase_intro_2020")
cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor,执行SQL语句都是通过游标对象实现
sql = "SELECT VERSION();"  # 该SQL语句返回MySQL的安装版本，用以确定是否成功连接服务器
cursor.execute(sql)  # 执行SQL语句
result = cursor.fetchone()  # 获取单条数据
print(result)
