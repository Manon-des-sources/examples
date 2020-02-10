class Store():
    """商店模型"""
    def __init__(self, name, type, commodityList):
        """初始化商店属性"""
        self.name = name
        self.type = type
        self.commodityList = commodityList
    def openStore(self):
        print(self.name, "开始营业")
    def closeStore(self):
        print(self.name, "停止营业")
    def sell(self, comodity, quantity):
        """出售"""
        if comodity not in self.commodityList.keys():
            print("本商店没有" + comodity)
            return
        if self.commodityList[comodity] >= quantity:
            self.commodityList[comodity] -= quantity
            print("商品" + comodity + "出售了" + str(quantity) + "件")
        else:
            print("商品" + comodity + "数量不足")
    def stock(self, comodity, quantity):
        """进货"""
        if comodity not in self.commodityList.keys():
            self.commodityList[comodity] = quantity
            print("新增商品" + comodity + str(quantity) + "件")
            return
        self.commodityList[comodity] += quantity
        print("商品" + comodity + "进货了" + str(quantity) + "件")
    def showComodityList(self):
        print(self.name + "库存商品：")
        for comodity in self.commodityList:
            print(comodity, ':', self.commodityList[comodity], ",", end="")
        print("\r\n")