import logging

# 指定输出信息的级别：DEBUG、INFO、WARNING、ERROR
# INFO异常提示信息
logging.basicConfig(level = logging.INFO)

def levelFoo(data):
    print('leveFoo get input: ', data)
    return 10 / int(data)

def levelBar(data):
    print('leveBar get input: ', data)
    return levelFoo(data) * 4

def doMain(data):
    try:
        print(levelBar(data))
    except ValueError as e:
        # logging.exception(e)
        # 异常信息写入文本
        logging.info('data = 0')
        # logging.info(e)
    finally:
        print('finnaly')

# def mainDo(data):
#     levelBar(data)

# print(dir(logging))
doMain('a')
# mainDo('a')
print('end')
