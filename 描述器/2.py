import  inspect
def add(x:int , y:int ,*args,**kwargs) -> int:
    return x+y
sig=inspect.signature(add)
print(add.__annotations__)
print(sig,type(sig))
print(sig.parameters)
print("---------")
print(sig.parameters["y"],type(sig.parameters["y"]))
print(sig.parameters["y"].annotation)

