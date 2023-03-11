commands={}
def reg(name):
    def _reg(fn):
        commands[name]=fn
        return fn
    return _reg
@reg('mag')  #foo1()=@reg("mag")foo1()   函数执行 foo1()()
def foo1():
    return "welcome magedu"
print(commands)
