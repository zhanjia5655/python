import pymysql
conn=None
cursor=None
try:
    conn=pymysql.connect(user="root",password="123",host="192.168.56.1",database="mydb")
    print(conn.ping(False))
    cursor=conn.cursor()
    sql="insert into teachers value(002,3,'zhan','m')"
    line=cursor.execute(sql)
    print(line)
    conn.commit()
except:
    conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
