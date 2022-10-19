class ProductNode:
    def __init__(self, code, price):
        self.__check_data(code, price)

        self.__left = None
        self.__right = None
        self.__code = code
        self.__price = price

    def __check_data(self, code, price):
        if not isinstance(code, int):
            raise TypeError('Only type int allowed for product code.')
        if not isinstance(price, int | float):
            raise TypeError('Only types int and float allowed for price.')

    def printTree(self):
        if self.__left:
            self.__left.printTree()
        print('Product code: {0}; Price: {1}'.format(self.__code, self.__price))
        if self.__right:
            self.__right.printTree()

    def insert(self, code, price):
        self.__check_data(code, price)

        if self.__code:
            if code < self.__code:
                if self.__left is None:
                    self.__left = ProductNode(code, price)
                else:
                    self.__left.insert(code, price)
            elif code > self.__code:
                if self.__right is None:
                    self.__right = ProductNode(code, price)
                else:
                    self.__right.insert(code, price)
        else:
            self.__code = code

    def find(self, code, quantity):
        if not isinstance(quantity, int):
            raise TypeError('Only type int allowed for quantity.')
        if code == self.__code:
            return self.__price * quantity
        if code < self.__code:
            if self.__left:
                return self.__left.find(code, quantity)
        else:
            if self.__right:
                return self.__right.find(code, quantity)
        raise ValueError('Searched code doesn\'t exist in this tree.')