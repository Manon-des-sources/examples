from store  import Store
# 调用另一个目录的模块
from common.common import CommonFun

# 继承基类
class FoodStore(Store):
    """食品店"""
    def __init__(self, name, type, comodityList):
        # 调用基类的初始化接口、使得FoodStore这个类获得基类的属性和接口
        super().__init__(name, type, comodityList)
        # 子类专属属性定义
        self.greetings = "欢迎光临"
    def isFoodGood(self):
        print(self.greetings + ',' + "一人食好好吃\r\n")
    # 子类重写openStore方法、替代基类的openStore方法
    def openStore(self, weekDay):
        if weekDay == "星期天":
            print(weekDay + "不营业\r\n")
        else:
            print(self.name, "开始营业\r\n")


if __name__ == "__main__":
    # 陈氏商行
    myCommodityList = {'苹果':100, '牛奶':210, '毛巾': 72, '沐浴露':55}
    myStore = Store("陈氏商行", "超市", myCommodityList)
    # 访问类的变量
    print(myStore.name, myStore.type, myStore.commodityList, end="\r\n\r\n")

    myStore.sell("牛奶", 10)
    myStore.showComodityList()

    myStore.stock("西红柿", 200)
    myStore.showComodityList()

    myStore.stock("毛巾", 20)
    myStore.showComodityList()

    # 直接运行一个类、而不需要任何实例
    CommonFun().SplitLine()

    # 一人食
    foodComodityList = {'牛肉干':100, '饭团':210, '烤肉粒': 72, '菜心':55}
    onePersonFood = FoodStore("一人食", "食品店", foodComodityList)
    print(onePersonFood.name, onePersonFood.type, onePersonFood.commodityList, end="\r\n\r\n")
    onePersonFood.isFoodGood()
    onePersonFood.openStore("星期天")
    # 访问类的变量
    onePersonFood.greetings = "新年好"
    print(onePersonFood.greetings, end="\r\n\r\n")

    onePersonFood.sell("饭团", 200)
    onePersonFood.showComodityList()

    onePersonFood.stock("千页豆腐", 50)
    onePersonFood.showComodityList()


    CommonFun().SplitLine()
    