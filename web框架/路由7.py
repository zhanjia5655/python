from webob import Response , Request,dec,exc
from wsgiref.simple_server import make_server
#框架
class Application:
    #路由表
    ROUTETABLE={}
    @classmethod#类装饰器 Application.register()
    def register(cls,path):
        def wrapper(handler):
            cls.ROUTETABLE[path]=handler #装饰器的作用就是增加字典
            print("123")
            return handler
        return wrapper

    @dec.wsgify#实例化调用
    def __call__(self,request:Request):
        try:
            return self.ROUTETABLE.get(request.path)(request) #返回的是函数调用
        except:
            raise exc.HTTPNotFound("您访问的页面不存在")
#服务器配置文件：
@Application.register("/")  #index=Application.register("/")(index) ,程序加载就会注册,调用执行装饰后的函数，之前的实验区别是被装饰的函数调用了，一起执行
def index(request:Request):
    res=Response()
    res.body="<h1>根目录页面</h1>".encode()
    return  res
@Application.register("/python")
def showpython(request:Request):
    res=Response()
    res.body="<h1>测试“python”页面</h1>".encode()
    return  res
#用户注册：
# Application.register("/",index)
# Application.register("/python",showpython)
#print(Application.__dict__)
if __name__ == "__main__":
    ip="127.0.0.1"
    port=9999
    server=make_server(ip,port,Application())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:server.server_close()