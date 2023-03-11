class ModelMeta(type):
    def __new__(cls, name, bases, dict):
        print(1,cls)
        print(2,name)
        print(3,bases)
        print(4,dict)
        b=10
        return super().__new__(cls, name, bases, dict)
class A(metaclass=ModelMeta): #用元类构建自己的类
    a=10
    def __init__(self):
        pass
    pass
class B(A):
    pass
print(type(B),type(A))

