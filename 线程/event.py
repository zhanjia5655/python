
from threading import Event,Thread
import logging
import time
import time
FORMAT="%(asctime)s%(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)

def boss(event:Event):

    logging.info("I'm boss ,waiting for U")
    print(event.is_set())
    # while not event.wait(3):每几秒判断一次false
    #     print('aaa')
    #     print(event.is_set())
    print('boss1',event.is_set())
    event.wait(5) #等待过程中，阻塞住5秒，event.is_set()一直为false，只是未执行，等到超时为false 除非是set（）退出循环执行条件，不然一直是false  #while not event.is_set(5) 每5秒执行一次
    print('boss2',event.is_set()) #如果在规定的时间（10s）内执行了event set 则返回true 如果规定时间内（3s）未执行完，则返回 flase，只要看是否在规定时间内执行了 event set
    logging.info("Good job")

# def worker(event:Event,count=3):
#     logging.info("I'm working for U")
#     cups=[]
#     while True:
#         logging.info("make 1")
#         logging.info(event.is_set())
#         time.sleep(1)
#         cups.append(1)
#         if len(cups)>=count:
#             event.set()
#             break
#     logging.info("I'm finished my job ,cpus={}".format(cups))
event=Event()
# w=Thread(target=worker,args=(event,10))
b=Thread(target=boss,args=(event,))
# w.start()
b.start()

# boss 和 worker使用的同一个event ，如果不同就不能这么操作
