# 多表联合查询
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, create_engine,func
from sqlalchemy.orm import sessionmaker,relationship
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
    dept_emps=relationship('Dept_emp')#要打印这一项 不然第二个表中的数据展示不了，一对多的关系，它是用列表保存多个值，引号中加入另外一个类的名称
    # 第一参数是字段名，如果和属性名不一致，一定要指定
    # age = Column('age', Integer)
    def __repr__(self):
        return "{} no={} name={} {} gender={} dept_emps={}".format(
            self.__class__.__name__, self.emp_no, self.first_name, self.last_name,
            self.gender.value,self.dept_emps
        )
class Department(Base):
    __tablename__ = 'departments'
    dept_no = Column(String(4), primary_key=True)
    dept_name = Column(String(40), nullable=False, unique=True)
    def __repr__(self):
        return "{} no={} name={}".format(
            type(self).__name__, self.dept_no, self.dept_name)
class Dept_emp(Base):
    __tablename__ = "dept_emp"
    emp_no = Column(Integer, ForeignKey('employees.emp_no',ondelete='CASCADE'),primary_key=True)#外键 表名.字段
    dept_no = Column(String(4), ForeignKey('departments.dept_no', ondelete='CASCADE'),primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)
    def __repr__(self):
        return "{} empno={} deptno={}".format(
            type(self).__name__, self.emp_no, self.dept_no)
ForeignKey('employees.emp_no', ondelete='CASCADE') #定义外键约束
# 打印函数
def show(emps):
    for x in emps:
        print(x)
    print('~~~~~~~~~~~~~~~',end='\n\n')

# 查询10010员工所在的部门编号
# results = session.query(Employee, Dept_emp).filter(Employee.emp_no == Dept_emp.emp_no).filter(Employee.emp_no == 10010).all()
# show(results)
# 2.join方法
# 查询10010员工所在的部门编号
# 第一种写法(别用 )
#results = session.query(Employee).join(Dept_emp).filter(Employee.emp_no == 10010).all()
# 第二种写法(推荐)
#results = session.query(Employee).join(Dept_emp, Employee.emp_no ==Dept_emp.emp_no).filter(Employee.emp_no == 10010).all()
# 第三种
#results = session.query(Employee).join(Dept_emp, (Employee.emp_no == Dept_emp.emp_no) &(Employee.emp_no == 10010)).all()
show(results)

