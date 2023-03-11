

import multiprocessing
import datetime
def calc(i):


for i in range（10）:


    sum=0
    for _ in range(10):
        sum+=1
        print(multiprocessing.current_process())
if __name__ == "__main__":
    start =datetime.datetime.now()
    lst=[]
    for i in range(5):
        p=multiprocessing.Process(target=calc,args=(i,),name="p-{}".format(i))
        p.start()
        lst.append(p)
    for p in lst:
        p.join()
    delta=(datetime.datetime.now()-start).total_seconds()
    print(delta)
