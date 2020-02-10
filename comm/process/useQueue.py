#!/usr/bin/python3
# coding = utf-8

# 子进程之间的通信.Queue

from multiprocessing import Process
from multiprocessing import Queue
import random
import time
import os

# 这个进程往Queue里写数据
def pWrite(q):
    print("Write Process [%s]" % os.getpid())
    for value in ['A', 'B', 'C']:
        print('to Queue Put %s!' % value)
        q.put(value)
        time.sleep(random.random())

# 这个进程从Queue里取出数据
def pRead(q):
    print("Read Process [%s]" % os.getpid())
    while True:
        value = q.get(True)
        print('from QUeue Get %s.' % value)

if __name__ == "__main__":
    # 创建Queue、各子进程共同使用
    q = Queue()
    # (target(args))
    pw = Process(target=pWrite, args=(q,))
    pr = Process(target=pRead,  args=(q,))
    # 启动子进程
    pw.start()
    pr.start()
    pw.join()
    # 结束pr的死循环
    pr.terminate()
