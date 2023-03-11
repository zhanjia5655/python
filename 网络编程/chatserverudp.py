import socket
import threading
import datetime
import logging
#p246
logging.basicConfig(format="%(thread)s%(threadName)s%(message)s",level=logging.INFO)
class ChatServerUdp:
    def __init__(self,ip,port,interval):
        self.ip=ip
        self.port=port
        self.addr=(self.ip,self.port)
        self.sock=socket.socket(type=socket.SOCK_DGRAM)
        self.event=threading.Event()
        self.clients={}
        self.interval=interval
  #      self.clients=set() #去重，集合

    def start(self):
        self.sock.bind(self.addr)
        threading.Thread(name="recvfrom",target=self._recv).start()
    def stop(self):
        self.sock.close()
        self.event.set() #evnet.is_set 重置为true
    def _recv(self):
        while not self.event.is_set():
            data,clientaddr =self.sock.recvfrom(1024)
            logging.info(clientaddr)
            data=data.decode().strip()
            current=datetime.datetime.now().timestamp()
            if data =="^hb^":#心跳机制，客户端每个一段时间发一个数据包连接
                self.clients[clientaddr]=current
                continue
            if data =="quit":
                self.clients.pop[clientaddr]
                continue
            if data =="come":
                self.clients[clientaddr]=current
                continue
            self.clients[clientaddr]=current

            msg="{}".format(data.decode(encoding="gb2312"))
            logging.info(msg)
            now=datetime.datetime.now().timestamp()
            lst=set()
#            for c in self.clients:#群发
            for caddr,ts in self.clients.items():
                if now - ts <= self.interval:#如果在活动的客户端群发消息，没活动的从dict中删除
                    self.sock.sendto(msg.encode(encoding="gb2312"),caddr)
                else:
                    lst.add(caddr)
            for x in lst:
                self.clients.pop(x) #不能一边迭代一边修改迭代，建一个临时区加进去，然后再删除，巧妙！！！！

 #                    self.sock.sendto(msg.encode(encoding="gb2312"),clientaddr)
# now=datetime.datetime.now().timestamp()
# threading.Event().wait(8)
# tt=datetime.datetime.now().timestamp()-now
# logging.info(tt)

# logging.info(datetime.datetime.now().timestamp())

cs=ChatServerUdp("127.0.0.1",9988,10)
cs.start()

while True:
    cmd= input(">>>>>").strip()
    if cmd =="quit":
        cc.stop()
        break


