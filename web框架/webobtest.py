from webob import Response , Request,dec
from wsgiref.simple_server import make_server

@dec.wsgify
def app(request:Request):
    print(request.path)
    # / favicon.ico
    # 127.0.0.1 - - [20 / Nov / 2021 12: 15:01] "GET /favicon.ico HTTP/1.1" 200 21
    return Response("<h1>网站测试</h1>")

if __name__ == "__main__":
    ip="127.0.0.1"
    port=9999
    server=make_server(ip,port,app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:server.server_close()