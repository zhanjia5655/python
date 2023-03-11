##########
# windows监控端口 netstat -anp tcp | find "9999"  视频 242
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
        self.event = threading.Event()
    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        threading.Thread(target=self._accept,name="accept").start()
    def stop(self):
        for c in self.clients.values():
            c.close()
        self.sock.close()
        self.event.wait(3)
        self.event.set()  #执行stop后 event.is_set重置为1，后期就不会再进新进程_accept, _recv
    def _accept(self):
        while not self.event.is_set(): #（可能是这样,is_set只有 set才能重置状态） 一直是false,
            logging.info(self.event.is_set())
            conn,client= self.sock.accept()
            logging.info(self.event.is_set())
            self.clients[client]=conn
            threading.Thread(target=self._recv,args=(conn,client),name="recv").start()
    def _recv(self,conn,client):  #<socket.socket fd=528, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9999), raddr=('127.0.0.1', 65244)>
        while not self.event.is_set():
            data=conn.recv(1024).decode(encoding="gb2312")
            logging.info(data)
            if data =="quit":#客户端退出
                self.clients.pop(client)
            msg = "ack {}".format(data)
            for c in self.clients.values():
                c.send(msg.encode(encoding="gb2312"))
cs= ChatServer()
cs.start()
def showthreads():
    while True:
        time.sleep(3)
        logging.info(threading.enumerate())
threading.Thread(target=showthreads,daemon=True).start()

while True:#后端退出
    cmd=input(">>>>").strip()
    if cmd =="quit"
        cs.stop()
        break




