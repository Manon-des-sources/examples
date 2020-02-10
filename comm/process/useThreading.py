#!/usr/bin/python3
# coding = utf-8

import threading
import time

# 新的线程
def newThread():
    print('thread is running [%s]' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread ended [%s]' % threading.current_thread().name)

# 每个进程都会默认启动1个线程：MainThread
print('thread is running [%s]' % threading.current_thread().name)
# 主线程启动/创建1个线程
t = threading.Thread(target=newThread, name='newThread')
t.start()
t.join()
# MainThread
print('thread ended [%s]' % threading.current_thread().name)