from webob import Response , Request,dec,exc
from wsgiref.simple_server import make_server
import re
#框架
class Application:
    #路由表
    ROUTETABLE=[]
    @classmethod#类装饰器 Application.register()
    def register(cls,pattern):
        def wrapper(handler):
            cls.ROUTETABLE.append((re.compile(pattern),handler))
            return handler
        return wrapper

    @dec.wsgify#实例化调用
    def __call__(self,request:Request):
        for pattern,handler in self.ROUTETABLE:
            if pattern.match(request.path):
                print(request.path)
                return handler(request)
        raise exc.HTTPNotFound("您访问的页面不存在")
    # aa=re.compile("/python")
    # print(aa.match("/python123"))
#服务器配置文件：
@Application.register("^/python$")
def showpython(request:Request):
    res=Response()
    res.body="<h1>测试“python”页面</h1>".encode()
    return  res
@Application.register("^/$")
def index(request:Request):
    res=Response()
    res.body="<h1>根目录页面1</h1>".encode()
    return  res
#用户注册：
# Application.register("/",index)
# Application.register("/python",showpython)
print(Application.__dict__)
if __name__ == "__main__":
    ip="127.0.0.1"
    port=9999
    server=make_server(ip,port,Application())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:server.server_close()