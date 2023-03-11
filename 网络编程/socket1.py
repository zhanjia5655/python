##########
# windows监控端口 netstat -anp tcp | find "9999"
import  threading
import time
import sys
import socket
import  logging

logging.basicConfig(format="%(thread)s%(threadName)s%(message)s",level=logging.INFO)


class ChatServer:
    def __init__(self,ip="127.0.0.1",port=9999):
        self.sock=socket.socket()
        self.addr=(ip,port)
        self.clients= {}
        self.event=threading.Event()
    def start(self):
        while not self.event.wait(1):
            self.sock.bind(self.addr)
            self.sock.listen()
            threading.Thread(target=self._accept,name="accept").start()
    def _accept(self):
        while not self.event.wait(1):
            conn,client= self.sock.accept()
            self.clients[client]=conn
            threading.Thread(target=self._recv,args=(conn,),name="recv").start()
    def _recv(self,conn):  #<socket.socket fd=528, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9999), raddr=('127.0.0.1', 65244)>
        while True:
            data=conn.recv(1024)
            logging.info(data.decode(encoding='gb2312'))
            msg = "ack {}".format(data)
            for conn in self.clients.values():
                conn.send(msg.encode())

cs= ChatServer()
cs.start()

def showthreads():
    while True:
        time.sleep(3)
        logging.info(threading.enumerate())
showthreads()
