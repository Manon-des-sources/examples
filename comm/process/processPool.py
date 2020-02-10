#!/usr/bin/python3
# coding = utf-8

from multiprocessing import Pool
import random
import time
import os

def longTime_Task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    t = random.random()*3
    print("task %s sleep %f seconds" % (name, t))
    time.sleep(t)
    end = time.time()
    print("task %s runs %0.2f seconds." % (name, end-start))

if __name__ == "__main__":
    print("Parent process is %s" % os.getpid())
    # 允许同时运行的子进程数量 = 4
    # 不设置的话、默认大小为CPU内核数
    # p = Pool()
    p = Pool(4)
    # 允许同时运行的子进程数量可以大于CPU内核数
    # p = Pool(6)
    # 启动6个子进程、前4个进程会立即执行、4个之后的进程要等到前面的进程结束并腾出位置后才启动
    for i in range(6):
        p.apply_async(longTime_Task, args=(i,))
    print("Waiting for all subprocesses end...")
    # 禁止再添加子进程
    p.close()
    # 等待所有子进程结束
    # p.join()
    # 不等待子进程结束的话、这里要延时等待才可以看到子进程打印的信息
    time.sleep(5)
    print("All subprocesses end")
    print("Parent process end %s" % os.getpid())

# Parent process is 1056
# Waiting for all subprocesses end...
# Run task 0 (8504)...
# task 0 sleep 1.920903 seconds
# Run task 1 (3852)...
# Run task 2 (7232)...
# task 1 sleep 0.161657 seconds
# task 2 sleep 2.057959 seconds
# Run task 3 (8240)...
# task 3 sleep 1.346724 seconds
# task 1 runs 0.16 seconds.
# Run task 4 (3852)...
# task 4 sleep 2.773177 seconds
# task 3 runs 1.35 seconds.
# Run task 5 (8240)...
# task 5 sleep 0.456089 seconds
# task 5 runs 0.46 seconds.
# task 0 runs 1.92 seconds.
# task 2 runs 2.06 seconds.
# task 4 runs 2.77 seconds.
# All subprocesses end
# Parent process end 1056