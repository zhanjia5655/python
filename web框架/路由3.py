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
    res.status_code=404
    res.body="Not Found".encode()
    return res
ROUTETABLE={
    "/":index,
    "/python":showpython
}
@dec.wsgify
def app(request:Request):
    # print(request.path)
    # res = Response()
    # if request.path=="/":
    #     return index(request)
    # elif request.path=="/python":
    #     return showpython(request)
    # else:
    #     return Notfond(request)
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