from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.topping_list = []
        size_prices = {"S": 8.00, "M": 10.00, "L": 12.00}
        self.price = size_prices[self.size]
    def addTopping(self, topping):
        self.topping_list.append(topping)
        topping_prices = {"S": 0.50, "M": 0.75, "L": 1.00}
        self.price += topping_prices[self.size]
    def getPizzaDetails(self):
        if self.topping_list == []:
            return f"CUSTOM PIZZA\nSize: {self.size}\nToppings:\nPrice: ${self.price:.2f}\n"
        else:
            s = ""
            for i in self.topping_list:
                s += f"\t+ {i}\n"
            return f"CUSTOM PIZZA\nSize: {self.size}\nToppings:\n" + s + f"Price: ${self.price:.2f}\n"
        
