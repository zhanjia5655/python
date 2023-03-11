from webob import Response , Request,dec
from wsgiref.simple_server import make_server

@dec.wsgify
def app(request:Request):
    print(request.path)
    res = Response()
    if request.path=="/":
        res.body="<h1>测试1页面</h1>".encode()
    elif request.path=="/python":
        res.body="<h1>测试“python”页面</h1>".encode()
    else:
        res.status_code==404
        res.body="Not Found".encode()
    return res
if __name__ == "__main__":
    ip="127.0.0.1"
    port=9999
    server=make_server(ip,port,app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:server.server_close()

