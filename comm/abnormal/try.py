# 跨越调用层级去捕获错误
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
        print('except: ', e)
    finally:
        print('finnaly')

def mainDo(data):
    levelBar(data)

def getResult():
    try:
        return 10 / 0
    except ZeroDivisionError:
        raise ValueError('input error')


doMain('a')
# mainDo('a')

getResult()

print('end')
