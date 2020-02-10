#!/usr/bin/python3
# coding = utf-8

# 创建一个聊天系统
# master

import random
import queue
import time

from multiprocessing.managers import BaseManager

# 用于向子机发送任务
msgQueue = queue.Queue()

# 用于接收结果

class QueueManager(BaseManager):
    pass

def msgQueueFun():
    return msgQueue


if __name__ == "__main__":
    # 把Queue注册到网络、并给她们命名
    QueueManager.register('get_msgQueue', callable=msgQueueFun)
    # 绑定端口5000、设置验证码b'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()

    # 获取可通过网络访问的Queue对象
    masgerQueue = manager.get_msgQueue()
    while True:
        # 主机先发起通信
        msgMe = input('Me: ')
        masgerQueue.put(msgMe)
        time.sleep(1)
        # 阻塞式等待
        msgSomeOne = masgerQueue.get(True)
        print('SomeOne: %s' % msgSomeOne)