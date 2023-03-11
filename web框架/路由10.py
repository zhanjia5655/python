from webob import Response , Request,dec,exc
from wsgiref.simple_server import make_server
import re
#框架
class Application:
    GET="GET"
    POST="POST"
    #路由表
    ROUTETABLE=[]
    @classmethod#类装饰器 Application.register()             cls.ROUTETABLE.append((method,re.compile(pattern),handler)) #正则表达式的编译后的 ,程序加载就会注册,调用执行装饰后的函数，之前的实验区别是被装饰的函数调用了，一起执行

    def register(cls,method,pattern):
        def wrapper(handler):
            cls.ROUTETABLE.append((method,re.compile(pattern),handler)) #正则表达式的编译后的
        #    print(cls.ROUTETABLE)
            return handler
        return wrapper
    @classmethod
    def get(cls,pattern):
       # print(cls)
        return cls.register("GET",pattern)
    # @classmethod
    # def post(cls,pattern):
    #     return cls.register("POST",pattern)
    @dec.wsgify#实例化调用
    def __call__(self,request:Request):
        for method,pattern,handler in self.ROUTETABLE:
            if request.method.upper()==self.GET:
                matcher=pattern.match(request.path)#正则表达式的编译后的
                if matcher:
                    return handler(request)
        raise exc.HTTPNotFound("您访问的页面不存在")
    # aa=re.compile("/python")
    # print(aa.match("/python123"))
#服务器配置文件,用户注册：
@Application.register("GET","^/python$")
# @Application.register("POST","^/python$")
@Application.get("^/python$")
# @Application.post("^/python$")
def showpython(request:Request):
    res=Response()
    res.body="<h1>测试“python”页面</h1>".encode()
    return  res
@Application.register("GET","^/$")
# @Application.register("POST","^/$")
@Application.get("^/$")
# @Application.post("^/$")
def index(request:Request):
    res=Response()
    res.body="<h1>根目录页面1</h1>".encode()
    return  res
print(Application.__dict__)
if __name__ == "__main__":
    ip="127.0.0.1"
    port=9999
    server=make_server(ip,port,Application())
    try:
        server.serve_forever() # __call__方法
    except KeyboardInterrupt:
        pass
    finally:server.server_close()

# [('GET', re.compile('^/python$'), <function showpython at 0x0000028A0ADB7820>),
#  ('GET', re.compile('^/python$'), <function showpython at 0x0000028A0ADB7820>),
#  ('GET', re.compile('^/$'), <function index at 0x0000028A0ADB78B0>),
#  ('GET', re.compile('^/$'), <function index at 0x0000028A0ADB78B0>)]