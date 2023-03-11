#表中增加记录
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
# 创建基类，便于实体类继承
Base = declarative_base()
#实体类
class Student(Base):
    #定义表名
    __tablename__ = 'student'
    #定义字段名
    id=Column(Integer,primary_key=True,nullable=False)
    name=Column(String(64))
    age=Column(Integer)
    def __repr__(self):
        return "{} id={} name={} age={}".format(self.__class__.__name__,self.id,self.name,self.age)
    __str__=__repr__

#引擎，管理连接池
host="192.168.56.1"
port=3306
user="root"
password="123"
database="mydb"
conn_str="mysql+pymysql://{}:{}@{}:{}/{}".format(user,password,host,port,database)

engine = sqlalchemy.create_engine(conn_str, echo=True)
#创建表
#Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)
Session=sessionmaker()
session=Session(bind=engine)
try:
    lis=[]
    for i in range(5):
        student=Student()
        student.name='tom'+str(i)
        student.age=20+i
        lis.append(student)
    session.add_all(lis)
    session.commit()
except Exception as e:
    print(e)
    session.rollback()
finally:
    pass