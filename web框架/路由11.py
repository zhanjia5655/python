from webob import Response , Request,dec,exc
from wsgiref.simple_server import make_server
import re
#框架
class Application:
    GET="GET"
    POST="POST"
    #路由表
    ROUTETABLE=[]
    @classmethod
    def route(cls,pattern,*methods):
        def wrapper(handler):
            cls.ROUTETABLE.append((methods,re.compile(pattern),handler)) #正则表达式的编译后的
        #    print(cls.ROUTETABLE)
            return handler
        return wrapper
    @classmethod
    def get(cls,pattern):
       # print(cls)
        return cls.route(pattern,"GET")
    @classmethod
    def post(cls,pattern):
        return cls.register(pattern,"POST")
    @dec.wsgify#实例化调用
    def __call__(self,request:Request):
        for methods,pattern,handler in self.ROUTETABLE:
            if not methods or request.method in methods:
                if request.method.upper()==self.GET:
                    matcher=pattern.match(request.path)#正则表达式的编译后的
                    if matcher:
                        return handler(request)
        raise exc.HTTPNotFound("您访问的页面不存在")
    # aa=re.compile("/python")
    # print(aa.match("/python123"))
#服务器配置文件,用户注册：
@Application.get("^/python$")
def showpython(request:Request):
    res=Response()
    res.body="<h1>测试“python”页面</h1>".encode()
    return  res
@Application.get("^/$")
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

