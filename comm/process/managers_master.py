#!/usr/bin/python3
# coding = utf-8

# master

import random
import queue
import time

from multiprocessing.managers import BaseManager

# 用于向子机发送任务
taskQueue = queue.Queue()

# 用于接收结果
resultQueue = queue.Queue()

class QueueManager(BaseManager):
    pass

def taskQueueFun():
    return taskQueue

def resultQueueFun():
    return resultQueue


if __name__ == "__main__":
    # 把两个Queue注册到网络、并给她们命名
    QueueManager.register('get_TaskQueue', callable=taskQueueFun)
    QueueManager.register('get_ResultQueue', callable=resultQueueFun)

    # 绑定端口5000、设置验证码b'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动Queue
    manager.start()

    # 获取可通过网络访问的Queue对象
    task   = manager.get_TaskQueue()
    result = manager.get_ResultQueue()

    # 放入数据到发送队列
    for i in range(10):
        n = random.randint(1, 1000)
        print('Put task %d' % n)
        task.put(n)

    # 看看接收结果里面有什么
    print('Try to get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)

    # 停止服务
    manager.shutdown()
    print('master exit!')
