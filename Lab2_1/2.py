import json
import os
import dataclasses
from datetime import datetime

BASE_PRICE = 100
ADDON_PRICE = 5

class Kitchen:
    def __init__(self, stock_info, log_input):
        if not os.path.isfile(stock_info):
            raise ValueError("Kitchen stock info doesnt exist")
        self.file_name = stock_info
        self.log_name = log_input
        with open(self.file_name, "r") as inp:
            self.__stock_info = json.load(inp)
        self.today_orders = []

    def __del__(self):
        with open(self.file_name, "w") as upd:
            json.dump(self.__stock_info, upd, indent=4)
        with open(self.log_name, "w") as log:
            json.dump(self.today_orders, log, indent=4)

    def available_addons(self, customer):
        addons = []
        base_required = dataclasses.asdict(self.get_order(customer, True))
        for keys in self.__stock_info.keys():
            if self.__stock_info[keys] > 1:
                if self.__stock_info[keys] - base_required[keys] > 0:
                    addons.append((keys, self.__stock_info[keys]))
        return addons

    def get_order(self, customer, *check, **kwargs):
        if not isinstance(customer, Customer):
            raise TypeError("Client should be customer type")
        price = BASE_PRICE + len(kwargs)*ADDON_PRICE
        match customer.date.weekday():
            case 0:
                obj = MondayPizza(price, **kwargs)
            case 1:
                obj = TuesdayPizza(price, **kwargs)
            case 2:
                obj = WednesdayPizza(price, **kwargs)
            case 3:
                obj = ThursdayPizza(price, **kwargs)
            case 4:
                obj = FridayPizza(price, **kwargs)
            case _:
                obj = WeekendPizza(price, **kwargs)
        required = dataclasses.asdict(obj)
        if not check:
            for keys in required.keys():
                if keys == 'price':
                    continue
                self.__stock_info[keys] -= required[keys]
                if self.__stock_info[keys] < 0:
                    raise ValueError("Required products not in stock")
            self.today_orders.append(dataclasses.asdict(obj))
        return obj


@dataclasses.dataclass(frozen=True)
class Customer:
    name: str
    date: datetime


@dataclasses.dataclass(frozen=True)
class Pizzabase:
    price: int
    sauce: int = 1
    cheese: int = 1
    beef: int = 0
    bbq_sauce: int = 0
    pepperoni: int = 0
    pepper: int = 0
    blue_cheese: int = 0
    ham: int = 0
    mushrooms: int = 0
    feta_cheese: int = 0
    cheddar_cheese: int = 0
    pork: int = 0
    sausage: int = 0
    bacon: int = 0

    def __str__(self):
        dictionary = dataclasses.asdict(self)
        return '  '.join([key+' '+str(dictionary[key]) for key in dictionary.keys() if dictionary[key]])


@dataclasses.dataclass(frozen=True, kw_only=True)
class MondayPizza(Pizzabase):
    pepperoni: int = 1
    pepper: int = 1


@dataclasses.dataclass(frozen=True, kw_only=True)
class TuesdayPizza(Pizzabase):
    pepperoni: int = 1
    blue_cheese: int = 1


@dataclasses.dataclass(frozen=True, kw_only=True)
class WednesdayPizza(Pizzabase):
    beef: int = 1
    bbq_sauce: int = 1


@dataclasses.dataclass(frozen=True, kw_only=True)
class ThursdayPizza(Pizzabase):
    ham: int = 1
    mushrooms: int = 1


@dataclasses.dataclass(frozen=True, kw_only=True)
class FridayPizza(Pizzabase):
    blue_cheese: int = 1
    feta_cheese: int = 1
    cheddar_cheese: int = 1


@dataclasses.dataclass(frozen=True, kw_only=True)
class WeekendPizza(Pizzabase):
    beef: int = 1
    pork: int = 1
    sausage: int = 1
    bacon: int = 1


file = "kitchen.json"
log = "orders.json"
rest = Kitchen(file, log)
maks = Customer("Jiji", datetime.now())
print(rest.available_addons(maks))
order = rest.get_order(maks, blue=1, pork=1)
print(order)