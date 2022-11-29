import time


t1 = time.time()
print(t1)
# 当前时刻与1970年1月1日0时0分0秒的差距秒数


t2 = time.localtime()
print(t2)
# 散列元组


t3 = time.asctime(time.localtime())
print(t3)


t4 = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
print(t4)
