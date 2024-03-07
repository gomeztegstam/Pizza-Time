from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
class PizzaOrder:
    def __init__(self, time):
        self.pizzas = []
        self.time = time
    def getTime(self):
        return self.time
    def setTime(self, time):
        self.time = time
    def addPizza(self, pizza):
        self.pizzas.append(pizza)
    def getOrderDescription(self):
        order_description = f"******\nOrder Time: {self.time}\n"
        for pizza in self.pizzas:
            order_description += f"{pizza.getPizzaDetails()}\n\n----\n"
        total_price = sum(pizza.getPrice() for pizza in self.pizzas)
        order_description += "TOTAL ORDER PRICE: ${total_price:.2f}\n******\n"
        return order_description



    def getOrderDescription(self):
        totalprice = 0.00
        order = f"******\nOrder Time: {self.time}\n"
        if self.pizzas != []:
            for pizza in self.pizzas:
                totalprice += pizza.getPrice()
                order += pizza.getPizzaDetails() + "\n----\n"
        order += f"TOTAL ORDER PRICE: ${totalprice:.2f}\n******\n"
        return order
