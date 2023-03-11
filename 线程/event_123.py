
from threading import Event,Thread
import time
import logging
logging.basicConfig(level=logging.INFO)

def do(event:Event,intervla:int):
    while not event.wait(intervla):
        logging.info("do sth")
        logging.info(e.is_set())


e=Event()
Thread(target=do,args=(e,3)).start()
e.wait(10)
e.set()
print(e.is_set())
print("main exit")
