
import pymysql
conn=pymysql.connect(user="root",password="123",host="192.168.56.1",database="mydb")
print(conn.ping(False))
# try:
#     conn=pymysql.connect(user="root",password="123",host="192.168.56.1",database="mydb")
#     # print(conn.ping(False))
#
# finally:
#     if conn:
#         conn.close()
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
conn.close()
