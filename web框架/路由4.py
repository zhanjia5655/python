from webob import Response , Request,dec
from wsgiref.simple_server import make_server

def index(request:Request):
    res=Response()
    res.body="<h1>测试1页面</h1>".encode()
    return  res
def showpython(request:Request):
    res=Response()
    res.body="<h1>测试“python”页面</h1>".encode()
    return  res
def Notfond(request:Request):
    res=Response()
    res.status_code=404
    res.body="Not Found".encode()
    return res
ROUTETABLE={
    # "/":index,
    # "/python":showpython
}
def register(path,handler):

    ROUTETABLE[path]=handler
register("/",index)
register("/python",showpython)

@dec.wsgify
def app(request:Request):
    return ROUTETABLE.get(request.path,Notfond)(request)
if __name__ == "__main__":
    ip="127.0.0.1"
    port=9999
    server=make_server(ip,port,app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:server.server_close()