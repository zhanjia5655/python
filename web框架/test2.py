class Context(dict):
    def __getattr__(self, item):
        try:
            return self[item]
        except :
            raise AttributeError("Attribute {} Not Found".format(item))
    def __setattr__(self, key, value):
        self[key]=value
a=Context()
a.ab=123
print(a.ab)