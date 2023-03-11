
import threading

def show_threads(n=5,event=threading.Event()):
    def _showthreads():
        # while not event.is_set():
        while not event.wait(n):
            print(threading.enumerate())
    threading.Thread(target=_showthreads,daemon=True,name="ShowThreads").start()

# class A:
#     def __init__(self):
#         print("123")
#         self.call()
#     def __call__(self, *args, **kwargs):
#         print("AAAA")
# class B(A):#B在实例化过程中，自己没有init，找父亲A的 init,self的call 是指B的实例化调用call 优先B
#     def __init__(self):
#         self.call()
#         super().__init__()
#         print("B init {}".format(super))
#     def call(self):
#         print("BBB")
#         print("B call {}".format(super))
#
# B()
