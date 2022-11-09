import json
import uuid
import datetime

class NoTickestLeftError(Exception):
    def __init__(self, message):
        self.message = message


class Customer:
    def __init__(self, name, surname, isstudent):
        self.name=name
        self.surname=surname
        self.isstudent=isstudent


    @property
    def name (self):
        return self.__name


    @name.setter
    def name (self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong type for 'name' atribute")
        self.__name = value


    @property
    def surname (self):
        return self.__surname


    @surname.setter
    def surname (self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong type for 'surname' atribute")
        self.__surname = value


    @property
    def isstudent (self):
        return self.__isstudent


    @isstudent.setter
    def isstudent (self, value):
        if not isinstance(value, bool):
            raise TypeError("Wrong type for 'isstudent' atribute")
        self.__isstudent = value


class Event:
    def __init__(self):
        with open("1.json", encoding="utf-8") as f:
            self.date = datetime.datetime(*list(map(int, json.load(f)["event"]["date"])))

    @staticmethod
    def find_already_bought_ticket(id: str):
        with open("database1.json", "r", encoding="utf-8") as f:
            database = json.load(f)
        ticket = database['event']['bought_tickets'][id]
        print(ticket)
        

    def generate_ticket(self, customer: Customer):
        date_delta = (self.date - datetime.datetime.now()).days
        if not date_delta > 0:
            raise ValueError("Too late to buy tickets")

        with open("1.json", 'r') as f:
            event_info = json.load(f)

        numb_of_tickets = event_info["event"]["tickets"]["amount"]
        
        if  numb_of_tickets <= 0:
            raise NoTickestLeftError("Tickets sold out!")
        
        numb_of_tickets -= 1
        event_info["event"]["tickets"]["amount"] -= 1
        
        with open("1.json", 'w') as f:
            json.dump(event_info, f)
        
        if customer.isstudent:
            return Student()
        elif date_delta > 60:
            return Advanced()
        elif date_delta < 10:
            return Late()
        else:
            return Regular()


class Ticket():
    def __init__(self):
        self.id = str(uuid.uuid1())


    @property
    def id(self):
        return self.__id


    @id.setter
    def id(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong type for 'id' atribute")
        self.__id = value


class Regular(Ticket):
    def __init__(self) -> None:
        super().__init__()
        with open("1.json", encoding="utf-8") as f:
            self.price = json.load(f)['event']['tickets']['regular']["cost"]
    
    def __str__(self):
        return f"Ticket: {self.id}\nPrice: {self.price}\n "

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong type for 'price' atribute")
        self.__price = value


class Advanced(Ticket):
    def __init__(self) -> None:
        super().__init__()
        with open("1.json", encoding="utf-8") as f:
            self.price = int(json.load(f)['event']['tickets']['advanced']["cost"])

    def __str__(self):
        return f"Ticket: {self.id}\nPrice: {self.price}\n "

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong type for 'price' atribute")
        self.__price = value

class Late(Ticket):
    def __init__(self) -> None:
        super().__init__()
        with open("1.json", encoding="utf-8") as f:
            self.price = int(json.load(f)['event']['tickets']['late']["cost"])

    def __str__(self):
        return f"Ticket: {self.id}\nPrice: {self.price}\n " 

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong type for 'price' atribute")
        self.__price = value


class Student(Ticket):
    def __init__(self) -> None:
        super().__init__()
        with open("1.json", encoding="utf-8") as f:
            self.price = int(json.load(f)['event']['tickets']['student']["cost"])

    def __str__(self):
        return f"Ticket: {self.id}\nPrice: {self.price}\n "

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong type for 'price' atribute")
        self.__price = value


class PaymentProcess:
    @staticmethod
    def buy_ticket(customer: Customer, event: Event):
        ticket = event.generate_ticket(customer)
        with open("database1.json", "r", encoding="utf-8" ) as f:
            ticket_data = json.load(f)
        if not ticket_data:
            ticket_data = {}
        if 'event' not in ticket_data:
            ticket_data['event'] = {}
        if 'bought_tickets' not in ticket_data['event']:
            ticket_data['event']['bought_tickets'] = {}
        if  str(ticket.id) not in ticket_data['event']['bought_tickets']:
            ticket_data['event']['bought_tickets'][str(ticket.id)] = {}
        ticket_data['event']['bought_tickets'][str(ticket.id)]['name'] = customer.name
        ticket_data['event']['bought_tickets'][str(ticket.id)]['surname'] = customer.surname
        ticket_data['event']['bought_tickets'][str(ticket.id)]['price'] = ticket.price
        ticket_data['event']['bought_tickets'][str(ticket.id)]['purchase_date'] = str(datetime.datetime.now())
        with open("database1.json", "w") as f:
            json.dump(ticket_data, f)


event = Event()

customer1 =  Customer("Dj", "Nick", True)
customer2 =  Customer("Jiji", "Mick", False)

process = PaymentProcess()
process.buy_ticket(customer1, event)
process.buy_ticket(customer2, event)

event.find_already_bought_ticket("9faf4e32-6036-11ed-8d22-a4db3077260c")
