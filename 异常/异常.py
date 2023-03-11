

class MyException(Exception):
    pass
    # def __init__(self,code,message):
    #     self.code=code
    #     self.message=message

# try:
#     raise MyException()
# # except MyException:
# #     print("catch the exception")
# except Exception:
#     print("exception")
def foo1():
    try:
        1/0
    # except MyException:
    #     print("catch the exception")
    # except Exception:
    #     print("exception")
    except ImportError:
        print("importerror")
    finally:
        print("finally")
try:
    foo1()
except Exception as e:
    print(e)
# except Exception:
#     print("exception")