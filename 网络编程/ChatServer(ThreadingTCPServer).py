import threading
from socketserver import ThreadingTCPServer, BaseRequestHandler
import sys
import time
import logging
import myutils


FORMAT = "%(asctime)s%(threadName)s%(thread)d%(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatHandler(BaseRequestHandler):
    clients = {}

    def setup(self):
        super().setup()
        self.event = threading.Event()
        self.clients[self.client_address] = self.request

    def finish(self):
        super().finish()
        self.clients.pop(self.client_address)
        self.event.set()

    def handle(self):

        super().handle()
        while not self.event.is_set():
            data = self.request.recv(1024).strip().decode()
            if data == "quit":
                logging.info("quit!")
                break
            msg = "ack {}".format(data)
            logging.info(msg)
            for c in self.clients.values():
                c.send(msg.encode())


class Chatserver:
    def __init__(self, addr=("127.0.0.1", 9999)):
        self.addr=addr
        self.chathandler=ChatHandler
        self.server=ThreadingTCPServer(self.addr, self.chathandler)
    def start(self):
        threading.Thread(target=self.server.serve_forever, name="ChatServer").start()
chat=Chatserver()
chat.start()
myutils.show_threads()
# addr = ("127.0.0.1", 9999)
# server = ThreadingTCPServer(addr, ChatHandler)
# threading.Thread(target=server.serve_forever, name="ChatServer").start()

