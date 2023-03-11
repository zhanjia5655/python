##########
# windows监控端口 netstat -anp tcp | find "9999"

import  threading
import time
import sys
import socket

import  logging

logging.basicConfig(format="%(thread)s%(threadName)s%(message)s",level=logging.INFO)

#logging.info('\xab\xc1#'.encode())
#TCP Server
sock = socket.socket() #1 服务器端
logging.info(sock)
ip="127.0.0.1"
port=9999
addr=(ip,port)
sock.bind(addr) #2
sock.listen() #3
#######################################

conn , addrinfo = sock.accept() #4默认阻塞，连接上就通过了
logging.info(conn) #客户端
logging.info(addrinfo)
for i in range(3):
    data=conn.recv(1024) #阻塞
    logging.info(data.decode(encoding='gb2312'))
    msg="ack{}".format(data)
    conn.send(msg.encode(encoding='gb2312'))

conn.close()
sock.close()
