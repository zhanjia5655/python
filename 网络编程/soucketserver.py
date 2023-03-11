
import myutils
import  socketserver
import  threading
import  logging
# FORMAT ="%(asctime)s%(theadName)s%(thread)d%(message)s"
# logging.basicConfig(format=FORMAT,level=logging.INFO)
FORMAT="%(thread)s%(threadName)s%(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)

class MyHander(socketserver.BaseRequestHandler):
    """hello"""
    def setup(self):
        super().setup()
        self.event=threading.Event()

    def handle(self):
        super().handle()
        print("-"*30)
        print(self.server,self.request,self.client_address)
        print("{}handler".format(self.__class__))
        print(self.__dict__)  #实例dict
        print(type(self).__dict__) #类的dict
        print(self.__class__.__base__)
        print(self.server.__dict__)
        print(threading.enumerate())
        print(threading.current_thread())
        print("-"*30)
        while not self.event.is_set():
            data=self.request.recv(1024)
            msg="Your msg ={}".format(data.decode()).encode()
            logging.info(data)
            self.request.send(msg)
addr=('127.0.0.1',9999)
server=socketserver.ThreadingTCPServer(addr,MyHander)  #MyHander是个类，没有看到实例化？？，从上面可以看出 肯定是实例化后才能调用handle方法
server.serve_forever() #新线程