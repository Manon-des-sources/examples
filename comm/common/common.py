class CommonFun():
    def __init__(self):
        """这里放置一些通用接口、以供平时使用"""
    def splitLine(self):
        print('-'*20)

import functools
def log(func):
    """使用装饰器"""
    @functools.wraps(func) # 将func的__name__等属性复制到下面的函数(wrapper)中
    def wrapper(self, *args, **kw): # 可以接受任意参数
        print("call %s()" % func.__name__)
        self.passLine()  # 增加self、就可以调用类的方法
        return func(self, *args, **kw)
    return wrapper

# 带参数的装饰器(需要返回一个高阶函数)
def logWith(text):
    """使用装饰器(带参数)"""
    def deco(func):
        @functools.wraps(func) # 将func的__name__等属性复制到下面的函数(wrapper)中
        def wrapper(*args, **kw):
            print("%s call %s()" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return deco

def logWithArgses(*text):
    """"包含log()和logWith()"""
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if len(text) > 0:
                print("%s call %s()" % (text[0], func.__name__))
            else:
                print("call %s()" % (func.__name__))
            return func(*args, **kw)
        return wrapper
    return deco

# 装饰器：begin call 和 end call
def logCall(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("begin call[%s]" % func.__name__)
        func(*args, **kw)
        print("end call[%s]" % func.__name__)
    return wrapper

# 使用枚举
from enum import Enum, unique
# 这个装饰器可以保证下面这个Enum中不会有value重复的成员
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 简单定义
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


class funUseage():
    def __init__(self):
        print("""这里用于测试一些方法和用法""")
    def passLine(self):
        print("passLine")
    def checkInputType(self, x):
        """使用内置函数检查输入类型"""
        if not isinstance(x, (int, float)):
            raise TypeError("bad oprand type")
    def returnMultiValue(self):
        """返回的多个参数是以tuple的方式返回的"""
        return 1, 2
    def useDefaultParam(self, name, age, city="hangzhou", country="china"):
        """默认参数(参数必须是不可变对象、否则每次调用后默认参数都会被修改)"""
        print("name:", name, "age:", age, "city:", city, "country:", country)
    def useVariableParam(self, name, age, *others):
        """可变参数：元组tuple"""
        print("name:", name, "age:", age, others)
    def useKeyParam(self, name, age, **others):
        """关键参数：字典dect"""
        print("name:", name, "age:", age, others)
    def useSlice(self, str):
        """使用切片操作删除字符串首尾的空格"""
        if str[0] == ' ':
            str = str[1:]
        if str[-1] == ' ':
            str = str[:-1]
        return str
    def creatGenerator(self, n):
        x, a, b = 0, 0, 1
        while x < n:
            # 每次运行到yield语句就返回
            yield b
            a, b = b, a + b
            x = x + 1
        return 'end'
    def creatGenerator_Triangle(self, n):
        i, num = 1, 0
        curList, outList = [0, 1, 0], [0, 1, 0]
        while i < n:
            yield outList[1:-1]
            outList = [0]
            x = 1
            while x < len(curList):
                num = curList[x-1] + curList[x]
                outList.append(num)
                x = x + 1
            outList.append(0)
            curList = outList
            i = i + 1
    def normalizeName(self, names):
        """把用户名修改为第一个字母大写、其他字母小写"""
        r = map(lambda s:s.lower(), names)
        names = list(r)
        # print(names)
        r = map(lambda s:s.replace(s[0], s[0].upper(), 1), names)
        names = list(r)
        # print(names)
        return names
    def prod(self, datas):
        """求数据list的积"""
        from functools import reduce
        return reduce(lambda x,y:x*y, datas)
    def str2float(self, fStr):
        """将字符串转换为浮点数"""
        d = {'0':1, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '.':"."}
        re = map(lambda s:d[s], fStr)
        re = list(re)
        Int = re[0:re.index('.')]
        Dec = re[re.index('.')+1:]
        l = len(Dec)
        print(re, l)
        from functools import reduce
        Int = reduce(lambda x,y:x*10+y, Int)
        print(Int)
        Dec = reduce(lambda x,y:x*10+y, Dec)
        print(Dec)
        re = Int + Dec/(10**l)
        return re
    def isOdd(self, data):
        return (data % 2) == 1
    def isEven(self, data):
        return (data % 2) == 0
    def oddGenerator(self):
        i = 1
        while True:
            i = i + 2
            yield i
    def notDivisible(self, data):
        """返回一个函数(相对于闭包)、这个闭包包含一个参数x"""
        """相当于下面这个定义"""
        return lambda x: (x % data) > 0
    def notDivisibleView(self, data):
        """用于解释上面这个没有显示定义参数x的定义方法"""
        def re(x):
            return (x % data) > 0
        return re
    def primesGenerator(self):
        yield 2
        lr = self.oddGenerator()
        while True:
            n = next(lr)
            yield n
            lr = filter(self.notDivisible(n), lr)  # 持续更新Iterator
    def primesGive(self, n):
        for x in self.primesGenerator():
            if x < n:
                print(x, end=' ')
            else:
                break
    def isPalindromeNum(self, data):
        """自然数回文判断"""
        s = str(data)
        left, right = 0, -1
        mid   = len(s) // 2
        count = mid
        if (mid % 2) == 1:
            count = count + 1
        while count > 0:
            count = count - 1
            if s[left] != s[right]:
                return False
            left  = left  + 1
            right = right - 1
        return True
    def palindromeNumGive(self, n):
        """自然数回文"""
        outNum = filter(self.isPalindromeNum, range(1, n))
        outNum = list(outNum)
        print(outNum)
    def lazy_sum(self, *args):
        """使用闭包(Closure)求和"""
        def sum():
            s = 0
            for data in args:
                s = s + data
            return s
        return sum
    def giveID(self):
        """闭包里面不要引用主函数里面会在后面变化的变量"""
        fl = []
        for i in range(0, 3):
            def id():
                return i+i
            fl.append(id)
        return fl
    def giveIDs(self):
        """闭包里面需要及时保存主函数里面会在后面变化的变量"""
        # fl = []
        # for i in range(0, 3):
        #     def ID(j):
        #         def id():
        #             return j+j
        #         return id
        #     fl.append(ID(i))
        # return fl
        def ID(j):
            def id():
                return j+j
            return id
        fl = []
        for i in range(0, 3):
            fl.append(ID(i))
        return fl
    def creatCounter(self):
        i = 0
        def counter():
            nonlocal i
            i = i + 1
            return i
        return counter
    # @logWithArgses("main")
    @logWithArgses()
    def helloWorld(self):
        print("hello world!")
    @logCall
    def helloGo(self):
        print("helloGo")
    def useEnum(self):
        print(dir(Enum))
        # Month继承了Enum的dir()属性
        print(dir(Month))
        for name, member in Month.__members__.items():
            print(name, '-+++->', member, ':', member.value)
        print(Weekday['Sun'], Weekday['Sun'].value, Weekday.Sun, Weekday.Sun.value, Weekday(1), Weekday(1).value)


# from cModule import getA

if __name__ == "__main__":
    fU = funUseage()

    # # 引用C文件
    # print(getA())

    # fU.useEnum()

    # fU.helloGo()

    # fU.helloWorld()
    # print(fU.helloWorld.__name__)

    # 闭包有参数的话、引用时也要传入参数
    # fn  = fU.notDivisible(10)
    # fnV = fU.notDivisibleView(10)
    # print(fn(2), fnV(5), fn(10), fnV(10))

    # counterA = fU.creatCounter()
    # counterC = fU.creatCounter()
    # print(counterA(), counterA(), counterA(), counterA())
    # print(counterC(), counterC(), counterC(), counterC())

    # fl0, fl1, fl2 = fU.giveIDs()
    # print(type(fl0), type(fl1), type(fl2))
    # print(fl0(), fl1(), fl2())
    # print(fl0 == fl1, fl0 == fl2, fl1 == fl2)  # 创建出来的闭包各自独立

    # fl0, fl1, fl2 = fU.giveID()
    # print(type(fl0), type(fl1), type(fl2))
    # print(fl0(), fl1(), fl2())

    # fsum = fU.lazy_sum(1,2,3,4,5,6,7,8,9)
    # print(type(fU.lazy_sum), type(fsum), fsum())

    # fU.palindromeNumGive(200)

    # fU.primesGive(20)

    # print(fU.str2float('12345.6789'))

    # print(fU.prod([3,5,7,9,11]))

    # names = ['liSa', 'ray', 'pOnY', "LLLiy", "NOEN"]
    # print('names = ', names)
    # print(fU.normalizeName(names))

    # # fU.checkInputType('A')
    # re = fU.returnMultiValue()
    # x, y = fU.returnMultiValue()
    # print(x, y, type(re))

    # fU.useDefaultParam("poney", 1)
    # others = ("suzhou", "china")
    # fU.useVariableParam("poney", 1, "hangzhou", "china")
    # fU.useVariableParam("poney", 1, *others)
    # fU.useKeyParam("buney", 10, city="hangzhou", country="china")
    # others = {"city":"suzhou", "country":"china"}
    # fU.useKeyParam("buney", 10, **others)

    # s = "  hello world!  "
    # print(fU.useSlice(s))
    # print(s.strip())

    # re = fU.creatGenerator(10)
    # print(type(re))
    # for i in re:
    #     print(i, end=' ')
    # print('\r\n')

    # re = fU.creatGenerator_Triangle(11)
    # for i in re:
    #     print(i)

