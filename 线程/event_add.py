from threading import Thread ,Event
import datetime
import logging
logging.basicConfig(level=logging.INFO)

def add(x:int,y:int):
    logging.info(x+y)
class Time:
    def __init__(self,interval,fn,*args,**kwargs):
        self.interval=interval
        self.fn=fn
        self.args=args
        self.kwargs=kwargs
        self.event=Event()
    def start(self):
        Thread(target=self._run()).start()
    def cancel(self):
        self.event.set()
    def _run(self):
        start=datetime.datetime.now()
        logging.info("waitting")
        self.event.wait(self.interval)
        if not self.event.is_set(): #刚开始为flase，当等待时间结束之前并没有执行event set命令，所以还是flase
            self.fn(*self.args,**self.kwargs)#注意* 结构参数
        dalta=(datetime.datetime.now()-start).total_seconds()
        logging.info("finished{}".format(dalta))

    # def __call__(self, *args, **kwargs):
    #     print(456)

t=Time(3,add,2,28)
t.start()