class A:
    b = 3
    def __init__(self):
        self.a1="a1"
        print("A.init")
    def __get__(self,instance,owner):
        print("A.__get__{}{}{}".format(self,instance,owner))
        return self
    def __set__(self,instance,value):
        print("A.__set__{}{}{}".format(self,instance,value))
        self.data=value
class B:
    x=A()
    def __init__(self):
        print("B.init")
        self.x="b.x" #会调用set方法
        self.y="b.x"
print("-------------------")
print(B.x.b)
print(B.x)
print("---------------------------------------")
b=B()
print("bbbbbbbbbbbbbb",b)
print(b.x.b) #调用get方法