AA="/abcd/123  1/"
#cc="abcd".replace()

print(AA.rstrip("/"))
import  re

aa=re.compile("/python\d")
print(aa)

class Context(dict):#字典属性化访问
    def __init__(self,d:dict):
        self.__dict__.update(d if isinstance(d,dict) else {})
        print(self.__dict__)
    def __getattr__(self, key):
        try:
            print(self.__dict__)
            return self.__dict__[key]
        except KeyError:
            raise AttributeError("Attribute {} Not Found".format(item))
    def __setattr__(self, key, value):
        self.__dict__[key]=value
dict1={"a":123,"b":45}
cc=Context(dict1)
print(cc.a)#cc.a 调用__getattr__方法
cc.a=99999
print(cc.a)


