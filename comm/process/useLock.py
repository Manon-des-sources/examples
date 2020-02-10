#!/usr/bin/python3
# coding = utf-8


import threading
import time

varE = 0
# 大家公用一把锁、使得同时只有一个线程可以打开这把锁
lock = threading.Lock()

def dealvarE(n):
    global varE
    varE += n
    varE -= n

def newThread(n):
    # 没有锁的情况下、这个运行次数足以导致varE的值不为0
    for i in range(1000000):
        # 试图开锁
        lock.acquire()
        try:
            # 开锁成功则执行、不成功则不执行
            dealvarE(n)
        finally:
            lock.release()

t1 = threading.Thread(target=newThread, args=(5,))
t2 = threading.Thread(target=newThread, args=(9,))
t1.start()
t2.start()
t1.join()
t2.join()
print(varE)