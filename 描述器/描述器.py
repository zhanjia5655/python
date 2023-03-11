
from functools import partial
class StaticMethod:
    def __init__(self,fn):
        print("__init__")
        self.fn=fn
    def __get__(self, instance, owner):
        print("__get__")
        return self.fn
class A:
    @StaticMethod #stmtd=StaticMethod(stmtd)
    def stmtd():
        print("stmtd")

class ClassMethod:
    def __init__(self,fn):
        print("__init__")
        self.fn=fn #stmtd
    def __get__(self, instance, owner):
        print("__get__")
        #return self.fn(owner)
        return partial(self.fn,owner) #因为stmtd函数没有返回值，返回空，上一行返回空，整个没有返回值，用偏函数将函数和参数返回去，等于返回一个新函数，没调用
class B:
    @ClassMethod #stmtd=ClassMethod(stmtd)
    def stmtd(cls):
        print(cls.__name__)
print("-----------------------")
f=B.stmtd
f()



