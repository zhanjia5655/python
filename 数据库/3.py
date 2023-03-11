import pymysql
from queue import Queue
conn = pymysql.connect(user="root",password="123",host="192.168.56.1",database="mydb")
cursor=conn.cursor()
with conn.cursor() as cursor:
    with cursor:
        insert_sql = "insert into teachers value(12,7,'zhan','m')"
        cursor.execute(insert_sql)
        conn.commit()
        sql = "select * from teachers"
        cursor.execute(sql)
        print(cursor.fetchall())


# 关闭
cursor.close()
conn.close()