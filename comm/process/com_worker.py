#!/usr/bin/python3
# coding = utf-8

# 创建一个聊天系统
# worker

import random
import queue
import time

from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    # 注册两个Queue、只能从网络上获取它们
    QueueManager.register('get_msgQueue')
    serverAdd = '127.0.0.1'
    print('Connect to sever %s ...' % serverAdd)
    worker = QueueManager(address=(serverAdd, 5000), authkey=b'abc')
    worker.connect()

    # 获取Queue对象
    workerQueue = worker.get_msgQueue()
    while True:
        # 阻塞式等待
        msgSomeOne = workerQueue.get(True)
        print('SomeOne: %s' % msgSomeOne)
        msgMe = input('Me: ')
        workerQueue.put(msgMe)
        time.sleep(1)
