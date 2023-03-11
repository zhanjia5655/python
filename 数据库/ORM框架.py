#Orm框架 表单 就是类，类的属性 就是字段 类的实例化就是一条条的记录
import pymysql
class Field:
    def __init__(self,name,filename=None,pk=False,unique=False,default=None,nullable=True,index=False):
        self.name=name
        if filename is None:
            self.filename=name
        else:
            self.filename=filename
        self.pk=pk
        self.unique=unique
        self.default=default
        self.nullable=nullable
        self.index=index
        print(2,self.__dict__)
    def validate(self,value):
        raise NotImplementedError
    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(4,self,instance,owner)
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name]=value
        print(5,self, instance, value)
    # def __str__(self):#这个类里的打印就会调用这个魔术方法
    #     return "{}{}".format(self.__class__.__name__,self.name)
    # __repr__ = __str__
class IntFiled(Field):
    def __init__(self,name,filename=None,pk=False,unique=False,default=None,nullable=True,index=False,auto_increment=False):
        self.aoto_increment=auto_increment
        super().__init__(name,filename,pk,unique,default,nullable,index)
    def validate(self,value):
        if value is None:
            if self.pk:
                raise TypeError("".format(self.name,value))
            if not self.nullable:
                raise TypeError()
        else:
            if not isinstance(value,int):
                raise TypeError()

class StringFiled(Field):
    def __init__(self,length=32, name=None, filename=None, pk=False, unique=False, default=None, nullable=True, index=False):
        self.length = length
        super().__init__(name, filename, pk, unique, default, nullable, index)

    def validate(self, value):
        if value is None:
            if self.pk:
                raise TypeError("".format(self.name, value))
            if not self.nullable:
                raise TypeError()
        else:
            if not isinstance(value, str):
                raise TypeError()
            if len(value) > self.length:
                raise ValueError("{} is too long value={}".format(self.name,value))

class Student:
    id=IntFiled("id")
    name=StringFiled(5,"name")
    age=IntFiled("age")
    def __init__(self,id,name="",age=""):
        self.id=id
        self.name=name
        self.age=age
        print(1,self.__dict__)
    # def save(self,conn:pymysql.connections.Connection):
    #     sql ="insert into student (id,name,age) value (%s,%s,%s)"
    #     try:
    #         with conn.cursor() as cursor:
    #             with cursor:
    #                 cursor.execute(sql,(self.id,self.name,self.age))
    #                 conn.commit()
    #     except:
    #         conn.rollback()
# conn = pymysql.connect(user="root",password="123",host="192.168.56.1",database="mydb")
xiaoming=Student(1,"xiao",20)
# xiaoming.save()
print(3,xiaoming.id,xiaoming.name,xiaoming.age,xiaoming,xiaoming.__class__)#调用了 __get__

#连接数据库
#