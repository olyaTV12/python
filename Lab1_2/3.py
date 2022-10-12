class Product:
    def __init__(self, price, description = ''):
        if not isinstance(price, int | float):
            raise TypeError('Only types int and float allowed for price.')
        if not isinstance(description, str):
            raise TypeError('Only type str allowed for description.')

        self.__price = price
        self.__description = description

    def __str__(self):
        return f'Price: {self.__price}, Desctiption: {self.__description}\n'

    @property
    def price(self):
        return self.__price


class Customer:
    def __init__(self, first_name, last_name, patronymic = '', phone_number = ''):
        if not all(isinstance(i, str) for i in [first_name, last_name, patronymic]):
            raise TypeError('Only type str allowed for names.')
        if not isinstance(phone_number, (str, int)):
            raise TypeError('Only types str and int allowed for phone number.')

        self.__first_name = first_name
        self.__last_name = last_name
        self.__patronymic = patronymic
        self.__phone_number = phone_number

    def __str__(self):
        return f'{self.__first_name} {self.__last_name} {self.__patronymic} {self.__phone_number} '


class Order:
    def __init__(self, person, *products):
        if not isinstance(person, Customer):
            raise TypeError('Only class Customer allowed for person info.')
        if not all(isinstance(i, Product) for i in products):
            raise TypeError('Only class Product allowed for product list.')

        self.__person = person
        self.__products = products

    def __str__(self):
        return f'Customer : {self.__person}\nProduct list :\n {" ".join(map(str, self.__products))}'

    def get_check(self):
        return sum([i.price for i in self.__products])
