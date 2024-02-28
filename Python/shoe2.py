class Shoe:
    def __init__(self,id,brand,model):
        self.__id = id
        self.__brand = brand
        self.__model = model
        self.__price = 0.00
        self.__discount = 0.00
        self.__net = 0.00
        self.__setPrice()
    def __setPrice(self):
        if self.__brand == "1":
            if self.__model == "1":
                self.__price = 1350.00
            elif self.__model == "2":
                self.__price = 1750.00
            elif self.__model == "3":
                self.__price = 4300.00
            else:
                self.__price = 4200.00
        elif self.__brand == "2":
            if self.__model == "1":
                self.__price = 1400.00
            elif self.__model == "2":
                self.__price = 2600.00
            elif self.__model == "3":
                self.__price = 1500.00
            else:
                self.__price = 1200.00
        elif self.__brand == "3":
            if self.__model == "1":
                self.__price = 1400.00
            elif self.__model == "2":
                self.__price = 2400.00
            elif self.__model == "3":
                self.__price = 2600.00
            elif self.__model == "4":
                self.__price = 1900.00
            else:
                self.__price = 1550.00
        elif self.__brand == "4":
            if self.__model == "1":
                self.__price = 2350.00
            elif self.__model == "2":
                self.__price = 5800.00
            elif self.__model == "3":
                self.__price = 3600.00
            else:
                self.__price = 2200.00
        else:
            if self.__model == "1":
                self.__price = 3800.00
            elif self.__model == "2":
                self.__price = 3600.00
            elif self.__model == "3":
                self.__price = 2100.00
            else:
                self.__price = 3600.00
        self.__setDiscount()
    def __setDiscount(self):
        if self.__brand == "1":
            if self.__model == "1":
                self.__discount = 0.05
            elif self.__model == "2":
                self.__discount = 0.05
            elif self.__model == "3":
                self.__discount = 0.08
            else:
                self.__discount = 0.08
        elif self.__brand == "2":
            if self.__model == "1":
                self.__discount = 0.10
            elif self.__model == "2":
                self.__discount = 0.15
            elif self.__model == "3":
                self.__discount = 0.10
            else:
                self.__discount = 0.15
        elif self.__brand == "3":
            if self.__model == "1":
                self.__discount = 0.10
            elif self.__model == "2":
                self.__discount = 0.20
            elif self.__model == "3":
                self.__discount = 0.20
            elif self.__model == "4":
                self.__discount = 0.20
            else:
                self.__discount = 0.10
        elif self.__brand == "4":
            if self.__model == "1":
                self.__discount = 0.20
            elif self.__model == "2":
                self.__discount = 0.30
            elif self.__model == "3":
                self.__discount = 0.30
            else:
                self.__discount = 0.20
        else:
            if self.__model == "1":
                self.__discount = 0.30
            elif self.__model == "2":
                self.__discount = 0.20
            elif self.__model == "3":
                self.__discount = 0.20
            else:
                self.__discount = 0.20
        self.__setNet()
    def __setNet(self):
        self.__net = self.__price - (self.__price * self.__discount)

    def getId(self):
        return self.__id

    def getBrand(self):
        brand = {
            '1': 'Puma',
            '2': 'Reebok',
            '3': 'Converse',
            '4': 'Adidas',
            '5': 'Nike'
        }
        self.__brand = brand[self.__brand]
        return self.__brand

    def getModel(self):
        model = {
            'Puma': ['Batman Suede', 'Basket Classic', 'Pokemon Rider', 'Minecraft'],
            'Reebok': ['Turbo Restyle', 'Zig Kinetica', 'GL 1000', 'Flexagon Force'],
            'Converse': ['Chuck Taylo All Star', 'Jack Purcell', 'Star Life Clean', 'Point Star',
                         'Star in Black Youth'],
            'Adidas': ['Neo', 'Stan Smith Lux', 'Forum Low', 'Run Falcon'],
            'Nike': ['Air Force', 'Air Max', 'Retro GTS', 'Free Run']
        }
        self.__model = model[self.__brand][int(self.__model) - 1]
        return self.__model

    def getPrice(self):
        return self.__price

    def getDiscount(self):
        self.__discount=self.__price*self.__discount
        return self.__discount

    def getNet(self):
        return self.__net

    def __str__(self):
        return ("Id: {0},Brand: {1},Model: {2},Price: {3:.2f},"
                "Discount: {4:.2f},Net: {5:.2f}").format(self.__id, self.__brand,self.__model,
        self.__price,self.__discount, self.__net)