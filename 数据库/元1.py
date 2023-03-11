# XClass = type('myclass', (object,), {'a':100, 'b':'string'})
# print(XClass)
# print(XClass.__dict__)
# print(XClass.__name__)
# print(XClass.__bases__)
# print(XClass.mro())

def __init__(self):
    self.x = 1000
    print(self.x)
def show(self):
    print(self.__dict__)
XClass = type('myclass', (object,), {'a':100, 'b': 'string', 'show':show, '__init__':__init__})
print(XClass)
print(XClass.__name__)
print(XClass.__dict__)
print(XClass.mro())
XClass().show()