# 一个类就是一种自定义的数据类型、和str等一样
# Python支持多重继承

# 没有需要继承的类、就继承object类
class Stu(object):
    # 只允许实例自己增加这几个属性
    # 也是可以被外界访问的属性
    __slots__ = ("__name", "__score", "__age", "showProperty")
    # 在创建实例的时候、self指向创建的那个示例本身
    def __init__(self, name, score):
        # 各种属性会自动绑定到self、也就绑定到了创建的那个示例本身
        # 以"__xx"开头的类变量只能在类内部使用、外部无法访问(实际变量名被解释器改为了_Stu__xx)
        self.__age   = 20
        self.__name  = name
        self.__score = score

    # 定制[print(Stu('name'))]时显示的内容
    def __str__(self):
        return 'Stu object [name: %s]' % self.__name
    # 定制在命令行使用[Stu('name')]时显示的内容
    __repr__ = __str__

    # 将实例本身转换为迭代对象返回
    def __iter__(self):
        return self
    # for...in循环中生效
    # 有了上面的__iter__、在for...in循环中就可以每一次执行一次下面的__next__
    def __next__(self):
        self.__age += 1
        if self.__age > 150:
            raise StopIteration()
        return self.__age

    # 可以像使用list[i]那样使用类(代码未完成、所以不支持切片)
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
    # 类似的还有__getitem__、__delitem__，使得类可以像tuple和dict那样使用

    # 实例可以作为函数调用
    # __call__生效
    def __call__(self):
        print("use %s" % self.__name)

    # 外部访问了类没有的属性时，会自动调用__getattr__
    def __getattr__(self, attr):
        if attr == 'event':
            return lambda:"event!"   # 可以返回一个函数
        elif attr == 'evt':
            return "!event"
        raise AttributeError('\'Stu\' object has no attribute \'%s\'' % attr)

    # 内置property装饰器
    @property
    def score(self):
        return self.__score
    # property创建另一个装饰器、用于把.setter方法变成属性(变量)
    @score.setter
    def score(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("score must be a number!")
        if value < 0 or value > 100:
            raise ValueError("score must be 0~100!")
        self.__score = value

    # property自带.getter方法
    # property没有定义.setter方法、那么这个属性就是一个只读属性(.getter)
    @property
    def age(self):
        # print(self.__age)
        return self.__age


class Animal(object):
    # 类属性：每个实例都可以访问、且访问的是同一个变量而不是实例自己的变量 
    # 下面的方法需要使用Animal.typeC的方式来访问
    typeC   = "Animal"
    members = 0
    def __init__(self, name):
        # 实例属性
        self.name = name
        print("hello %s [%s]" % (name, Animal.typeC))
        # 每增加一个实例、members加1
        Animal.members += 1
    def run(self):
        print("A animal is running...")
    def membersNum(self):
        print(Animal.members)

# 继承一个类
class Dog(Animal):
    # 自动获得基类的属性和方法
    pass

class Cat(Animal):
    def __init__(self, name):
        # 覆盖基类的__init__方法、但又需要基类的属性、就supper()一下、调用基类的__init__
        super().__init__(name)
    # 覆盖基类的方法、到时候就会调用这个新的方法：多态
    def run(self):
        print("A cat is running...")

# 参数是一个带有.run方法的变量/类(Python的动态语言特性允许animal参数可以不是Animal类)
# 只要是有.run方法的变量/类都可以被本函数调用：扩展
# 而实现方只需要实现自己的.run方法即可、不再考虑本函数是如何调用的(无需修改本函数)：封闭
def runTwice(animal):
    animal.run()
    animal.run()

def showProperty(self):
    print("property")

if __name__ == "__main__":
    Li = Stu("Li", 20)
    # __str__()起作用
    print(Li)
    # Python允许再绑定类以外的属性(变量/方法)
    # Li.age()
    print(Li.age)
    # Li.age = 10
    # # __next__生效
    # for i in Li:
    #     print(i)
    # __getitem__生效
    print(Li[0], Li[10])
    # __getattr__生效
    print(Li.event)
    print(Li.evt)
    # print(Li.e)
    # __call__生效
    if(callable(Li)):
        Li()

    from types import MethodType
    Li.showProperty = MethodType(showProperty, Li)
    Li.showProperty()
    # Li.level = "high"
    # property将score方法变成了属性(变量)
    Li.score = 60
    # Li.score = 111

    doggy = Dog('doggy')
    # 自动获得基类的属性和方法
    doggy.run()
    # doggy既是Dog类型、也是Animal类型(因为Dog也是一种Animal类型)
    print(isinstance(doggy, Animal), isinstance(doggy, Dog))

    catty = Cat('catty')
    print(catty.name)
    catty.run()
    print(isinstance(catty, Animal), isinstance(catty, Cat))

    # 调用各种有.run方法的变量/类
    runTwice(Animal("poney"))
    runTwice(doggy)
    runTwice(catty)
