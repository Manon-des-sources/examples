#!/user/bin/python3
# coding = utf-8

# 使用继承

class OldDog():
    def __init__(self):
        print("I'm a old dog!")
        self.hungry = True
    def eat(self):
        print("def eat(self):")
        if self.hungry == True:
            print("I eat it!")
            self.hungry = False
        else:
            print("No thanks, I'm not hungry!")

# 继承基类的方法
class NewDog(OldDog):
    def __init__(self):
        # 子类有了__init__()就不会调用基类的__init__()
        # 又需要使用基类的__init__()中的变量和实例、就需要使用super()显示调用一下基类的__init__()
        super().__init__()
        print("I'm a new dog!")
        # 初始化里面就可以调用下面定义的实例
        self.name()
    def name(self):
        print("my name")

if __name__ == "__main__":
    # olddog = OldDog()
    # olddog.eat()
    # olddog.eat()

    newdog = NewDog()
    newdog.eat()
    newdog.eat()