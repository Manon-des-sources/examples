#!/usr/bin/python3
# coding = utf-8

# 协程

# 消费者
# consumer 是一个生成器 generator
def consumer():
    r = ''
    while True:
        # 通过 yield 返回调用 生成器 的地方(按下F11进入)、调用者传过来的参数通过 yield 接收到 Nc
        Nc = yield r
        if not Nc:
            return
        print('[Consumer] consuming %s' % Nc)
        r = '200 ok ' + str(Nc)

# 生产者
def producer(c):
    # 启动生成器、进而调用 consumer，同时将参数传给生成器、生成器通过 yield 接收这个参数(按下F11进入)
    s = c.send(None)
    Np = 0
    while Np < 5:
        Np += 1
        print('[Producer] producing %s' % Np)
        # 启动生成器、进而调用 consumer，同时将参数传给生成器、生成器通过 yield 接收这个参数(按下F11进入)
        s = c.send(Np)
        print('[Producer] Consumer return %s' % s)
    c.close()

c = consumer()
producer(c)