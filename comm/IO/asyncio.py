#!/usr/bin/python3
# coding = utf-8

# asyncio + 协程 = 异步IO


import asyncio

# 把一个 generator 标记为 Coroutine类型，再把这个 Coroutine 放到 EventLoop 中
@asyncio.coroutine
def hello():
    print('Hello world!')
    # yield from 语法用于调用另一个 generator
    # 同时、asyncio.sleep() 也是一个 Coroutine、线程不会等到它返回、而是直接结束并执行 EventLoop 中的下一个消息循环或 Coroutine
    r = yield from asyncio.sleep(1)
    # 等到 asyncio.sleep() 返回后、线程从 yield from 得到返回值(None)、然后接着执行下面的这条语句
    print('Awake again!')

# 获取 EventLoop
loop = asyncio.get_event_loop()
# 执行协程
loop.run_until_complete(hello())
loop.close()