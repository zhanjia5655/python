import  selectors
import  socket
import  threading
import  myutils
selector=selectors.DefaultSelector()
#创建sock监听
sock=socket.socket()
ip="127.0.0.1"
port= 9990
addr=(ip,port)
sock.bind(addr)
sock.listen()
sock.setblocking(False)
e=threading.Event()
def accept(sock:socket.socket):
    conn,client=sock.accept()
    conn.setblocking(False)
    key=selector.register(conn,selectors.EVENT_READ,recv)
def recv(conn:socket.socket):
    data=conn.recv(1024).strip().decode()
    print(data)
    msg="Your msg={}".format(data)
    conn.send(msg.encode())
print(accept)
key=selector.register(sock,selectors.EVENT_READ,accept)
print(key)
myutils.show_threads()
while not e.is_set():
    events=selector.select()
    if events:
        print(events)
    for key,mask in events:
        print(key,mask)
        callback=key.data
        callback(key.fileobj)