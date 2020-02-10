#!/usr/bin/python3
# coding = utf-8

from multiprocessing import Process
import time
import os

def run_proc(name):
    t = 1
    print('Run child process %s (%s)!' % (name, os.getpid()))
    time.sleep(1)
    print("child run %d" % t)
    t += 1
    time.sleep(1)
    print("child run %d" % t)
    t += 1
    time.sleep(1)
    print("child run %d" % t)
    t += 1
    print("child process end!")

if __name__ == "__main__":
    # 当前在主进程
    print('Parent process is %s' % os.getpid())
    # 创建并运行子进程(target(args))
    p=Process(target=run_proc, args=('child_0',))
    print("Child process will be start：")
    p.start()
    print("Child process...")
    # # 等待子进程结束
    # p.join()
    # 等待子进程结束后、主进程继续运行
    print('end in process %s' % os.getpid())
    time.sleep(2)
    print("process end!")

# 
# 如果要往子进程里面传入一个对象、必须通过pickle传递
# 
