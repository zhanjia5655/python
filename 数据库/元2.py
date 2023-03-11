class ModelMeta(type):
    def __new__(cls, *args, **kwargs):
        print(1,cls)
        print(2,cls.__name__)
        print(3,args)
        print(4,kwargs)
        return super().__new__(cls, *args,**kwargs)

class A(metaclass=ModelMeta): #用元类构建自己的类
    a=10
    def __init__(self):
        pass
class B(A):
    def fun():
        print(111)
    fun()


print(type(B),type(A))
