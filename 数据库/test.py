
class Field:
    def __init__(self, fieldname=None, pk=False, nullable=True):
        self.fieldname = fieldname
        self.pk = pk
        self.nullable = nullable
    def __repr__(self):
        return "<Field {}>".format(self.fieldname)

a=Field(123)
print(a)

class ModelMeta(type): # 继承自type
    def __new__(cls, name, bases, dict):
        print(cls)
        print(name)
        print(bases)
        print(dict, '-------------')
        return super().__new__(cls, name, bases, dict)
class A:
    def fun():
        print(111)
    fun()