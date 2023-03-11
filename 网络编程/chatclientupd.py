import socket
import threading
import datetime
import logging
logging.basicConfig(format="%(thread)s%(threadName)s%(message)s",level=logging.INFO)
#sock=socket.socket(type=socket.SOCK_DGRAM)
# ip=("127.0.0.1")
# port=9988
# addr=(ip,port)
# data ="Udp1".encode()
# sock.connect(addr)#建立持续连接
# sock.send(data)#使用connect情况下才能使用
# #sock.sendto(data,addr) #不需要先建立连接，每次发送带有地址
# #data,caddr =sock.recvfrom(1024)
# data=sock.recv(1024)
# logging.info(data)
# #logging.info(data,caddr)
class ChatClientUdp:
    def __init__(self,ip="127.0.0.1",port=9988,intervla=5):
        self.sock=socket.socket(type=socket.SOCK_DGRAM)
        self.addr=(ip,port)
        self.event=threading.Event()
        self.interval=intervla
    def start(self0):
        threading.Thread(name="recvfrom",target=self._recv).start()
        threading.Thread(name="hb",target=self._sendhb,daemon=True).start() #主线程退出它也结束
    def _recv(self):
        while not self.event.is_set():
            data,addr=self.sock.recvfrom(1024)
            logging.info("{} {}".format(data,addr))
    def _sendhb(self):
        msg="^hb^"
        while not self.event.wait(self.interval):#每隔一段时间执行一次，wait 等待 如果超过时间内等到 返回true，没等到返回false
            self.sock.sendto(msg.encode(encoding="gb2312"),self.addr)
    def send(self,data="quit"):
        self.sock.sendto(data,self.addr)
    def stop(self):
        self.sock.close()
cc=ChatClientUdp()
cc.start()

while True:
    cmd= input(">>>>>").strip()
    if cmd =="quit":
        cc.send()
        cc.stop()
        break
    cc.send(cmd)
