
import threading ,logging,time
logging.basicConfig(level=logging.INFO,format="%(thread)d%(threadName)s%(message)s")

def work(s:threading.Semaphore):
    logging.info("in sub")
    s.acquire() #暂停执行
    logging.info("end sub")
s=threading.Semaphore(3)
logging.info(s.acquire())
logging.info(s.acquire())
logging.info(s.acquire()) #三次清零
threading.Thread(target=work,args=(s,)).start()

print("--------------")
time.sleep(2)
logging.info(s.acquire(False)) 跳过往后
logging.info(s.acquire(timeout=3))
s.release()
print("end main")
