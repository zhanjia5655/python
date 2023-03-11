from webob import Response , Request,dec,exc
from wsgiref.simple_server import make_server
#框架
class Application:
    #路由表
    ROUTETABLE={}
    @classmethod#类装饰器 Application.register()
    def register(cls,path,handler):
        cls.ROUTETABLE[path]=handler
    @dec.wsgify#实例化调用
    def __call__(self,request:Request):
        try:
            return self.ROUTETABLE.get(request.path)(request)
        except:
            print("1")
            raise exc.HTTPNotFound("您访问的页面不存在")
#服务器配置文件：
def index(request:Request):
    res=Response()
    res.body="<h1>测试1页面</h1>".encode()
    return  res
def showpython(request:Request):
    res=Response()
    res.body="<h1>测试“python”页面</h1>".encode()
    return  res
#用户注册：
Application.register("/",index)
Application.register("/python",showpython)
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