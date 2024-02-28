class Product:
    def __init__(self,id,brand,unit,desc,price,amount):
        self.__id=id
        self.__brand=brand
        self.__unit=unit
        self.__desc=desc
        self.__price=price
        self.__amount=amount
        self.__total=0.00
        self.__discount=0.00
        self.__net=0.00
        self.__setTotal()
    def __setTotal(self):
        self.__total=self.__price*self.__amount
        self.__setDiscount()
    def __setDiscount(self):
        if self.__total<1000:
            self.__discount=0
        elif self.__total<3000:
            self.__discount=self.__total*0.05
        elif self.__total<5000:
            self.__discount=self.__total*0.07
        else:
            self.__discount = self.__total * 0.10
        self.__setNet()
    def __setNet(self):
        self.__net=self.__total-self.__discount
    def getInfo(self):
        return "Id:{0},Brand:{1},Unit:{2},Description:{3},Price:{4},Amount:{5}".format(self.__id,
                self.__brand,self.__unit,self.__desc,self.__price,self.__amount)
    def getTotal(self):
        return self.__total
    def getDiscount(self):
        return self.__discount
    def getNet(self):
        return self.__net