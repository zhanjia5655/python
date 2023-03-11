import sys
import  threading
import time

def foo1():
    try:
        1/0
    finally:
        print("foo1 fin")
def foo2():
    time.sleep(4)
    try:
        foo1()
    finally:
        print("foo2 fin")
        open("abcde")
    while True:
        time.sleep(1)
t=threading.Thread(target=foo2)
t.start()
while True:
    time.sleep(1)
    print("-----------------------")
    if t.is_alive():
        print("alive")
    else:
        print("dead")