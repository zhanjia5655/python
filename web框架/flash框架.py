from webob import Response,Request,dec,exc
from wsgiref.simple_server import make_server
import re
class Router:
    def __init__(self,prefix:str=""):
        self._prefix=prefix
        self._routetable=[]
        #/product/tv/123  /product/tv/abc
        #/python/student/14
        #/product/(\w+)/(?P<id>\d+)

    @property
    def prefix(self):
        return self._prefix
    def route(self,pattern,*methods):
        def wrapper(handler):
            self._routetable.append((methods,re.compile(pattern,handler)))
            return handler
        return wrapper
    def get(self,pattern):
        return self.route("GET",pattern)
    def post(self,pattern):
        return self.route("POST",pattern)
    def match(self,request:Request) -> Response:
        if not request.path.startswith(self.prefix):
            return
        for methods,pattern,handler in self._routetable:
            if not methods or request.method.upper() in methods:
                matcher=pattern.match(request.path.replace(self.prefix))
                if matcher:
                    request.args=matcher.group()
                    request.kwargs=matcher.groupdict()
                    return handler(request)
class Application:
    ROUTERS=[]
    @classmethod
    def register(cls,router:Router):
        cls.ROUTERS.append(router)
