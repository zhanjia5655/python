
class Typed:
    def __init__(self,type):
        print(type)
        print(self)
        self.type=type
    def __set__(self, instance, value):
        print("A.__set__{}{}{}".format(self,instance,value))
        if not isinstance(value,self.type):
            raise ValueError(value)
    def __get__(self, instance, owner):
        print("A.__get__{}{}{}".format(self, instance, owner))
        return self.type
class Person:
    name =Typed(str)
    age=Typed(int)
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
print("-------------------------------")
p=Person("tom",18)
print(p.name,p.age)
print("-------------------------------")
import  inspect
print(inspect.signature(Person))
print(inspect.signature(Person).parameters)
params=inspect.signature(Person).parameters
for name,param in params.items():
    print(param,type(param))
    print(name, param.annotation)
