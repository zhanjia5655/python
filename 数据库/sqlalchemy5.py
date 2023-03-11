# 聚合函数
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
import enum
# 与或非
from sqlalchemy import or_, and_, not_
Base = declarative_base()
#引擎，管理连接池
host="192.168.56.1"
port=3306
user="root"
password="123"
database="test"
conn_str="mysql+pymysql://{}:{}@{}:{}/{}".format(user,password,host,port,database)

engine = create_engine(conn_str, echo=True)
Session=sessionmaker()
session=Session(bind=engine)
class MyEnum(enum.Enum):
    M = 'M'
    F = 'F'
class Employee(Base):
    # 指定表名
    __tablename__ = 'employees'
    # 定义属性对应字段
    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(MyEnum), nullable=False)
    hire_date = Column(Date, nullable=False)
    def __repr__(self):
        return "{} no={} name={} {} gender={}".format(
            self.__class__.__name__, self.emp_no, self.first_name, self.last_name,
            self.gender.value
        )
# 打印函数
def show(emps):
    for x in emps:
        print(x)
    print('~~~~~~~~~~~~~~~',end='\n\n')
from sqlalchemy import func
#count
# query = session.query(func.count(Employee.emp_no))
# print(query.one()) # 只能有一行结果
# print(query.scalar()) # 取one()返回元组的第一个元素
# max/min/avg
# print(session.query(func.max(Employee.emp_no)).scalar())
# print(session.query(func.min(Employee.emp_no)).scalar())
# print(session.query(func.avg(Employee.emp_no)).scalar())
# 分组 先分组 再count
#print(session.query(Employee.gender,func.count(Employee.emp_no)).group_by(Employee.gender).all())
