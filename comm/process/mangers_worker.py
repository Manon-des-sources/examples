#!/usr/bin/python3
# coding = utf-8

# worker

import random
import queue
import time

from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    # 注册两个Queue、只能从网络上获取它们
    QueueManager.register('get_TaskQueue')
    QueueManager.register('get_ResultQueue')

    serverAdd = '127.0.0.1'
    print('Connect to sever %s ...' % serverAdd)

    manager = QueueManager(address=(serverAdd, 5000), authkey=b'abc')
    manager.connect()

    # 获取Queue对象
    task   = manager.get_TaskQueue()
    result = manager.get_ResultQueue()

    # 从task队列获取master的任务数据
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d' % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is empty.')

    print('worker exit!')