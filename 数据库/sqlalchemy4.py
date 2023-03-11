#复杂查询
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
# 简单条件查询
# emps = session.query(Employee).filter(Employee.emp_no > 10015)
# AND 条件
#emps = session.query(Employee).filter(and_(Employee.emp_no > 10015, Employee.gender ==MyEnum.M))
#emps = session.query(Employee).filter((Employee.emp_no > 10015) & (Employee.gender == MyEnum.M))
#or条件
#emps = session.query(Employee).filter((Employee.emp_no > 10018) | (Employee.emp_no < 10003))
#emps = session.query(Employee).filter(or_(Employee.emp_no > 10018, Employee.emp_no < 10003))
# Not
#emps = session.query(Employee).filter(not_(Employee.emp_no < 10018))
#emps = session.query(Employee).filter(~(Employee.emp_no < 10018))
# in
# emplist = [10010, 10015, 10018]
# emps = session.query(Employee).filter(Employee.emp_no.in_(emplist))
# not in
# emps = session.query(Employee).filter(~Employee.emp_no.in_(emplist))
# like
#emps = session.query(Employee).filter(Employee.last_name.like('P%'))
# 排序
# 升序
#emps = session.query(Employee).filter(Employee.emp_no > 10010).order_by(Employee.emp_no)
#emps = session.query(Employee).filter(Employee.emp_no > 10010).order_by(Employee.emp_no.asc())
# 降序
# emps = session.query(Employee).filter(Employee.emp_no > 10010).order_by(Employee.emp_no.desc())
# 多列排序
# emps = session.query(Employee).filter(Employee.emp_no >10010).order_by(Employee.last_name).order_by(Employee.emp_no.desc())
# 分页
#emps = session.query(Employee).limit(4)
#应该是先偏移到18 然后再显示后四行
emps = session.query(Employee).limit(4).offset(18)
# 取所有数据
#print(emps.all()) # 返回列表，查不到返回空列表
# 取首行
#print(emps.first()) # 返回首行，查不到返回None
# # 有且只能有一行
#print(emps.one()) #如果查询结果是多行抛异常
#print(emps.limit(1).one())
# 删除 delete by query
#session.query(Employee).filter(Employee.emp_no > 10018).delete()
#session.commit() # 提交则删除
#show(emps)