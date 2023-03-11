

import  time
import  threading

def foo(n):
    for i in range(n):
        print(i)
        time.sleep(0.00001)
t1=threading.Thread(target=foo,args=(10,),daemon=True)
t1.start()
t1.join() #等t1执行完了，才能往后执行 ,daemon默认false 为true 主线程结束 子线程强行结束
print("main thread exiting")