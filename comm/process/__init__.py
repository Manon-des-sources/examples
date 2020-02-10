#!/usr/bin/python3
# coding = utf-8


import threading

# 为了避免一个线程一个全局变量、我们使用ThreadLocal
# 调用起来就像使用全局变量那样、但又是线程内独占的局部变量那样安全

# 创建全局ThreadLocal对象
localName = threading.local()

def processName(i):
    num = localName.num + 1
    if num != i:
        print("%s: num[%d] i[%d]" % (threading.current_thread().name, num, i))
    localName.num = i
    if i == 0 or i== 1:
        print('i = %d' % i)

def newThread(name):
    # 本线程绑定一个name对象到ThreadLocal对象
    localName.num = -1
    for i in range(10000000):
        processName(i)

if __name__ == "__main__":
    t1 = threading.Thread(target=newThread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=newThread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()