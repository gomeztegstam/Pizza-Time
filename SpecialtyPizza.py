from Pizza import Pizza
class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        size_prices = {"S": 12.00, "M": 14.00, "L": 16.00}
        self.price = size_prices[self.size]
    def getPizzaDetails(self):
        return f"SPECIALTY PIZZA\nSize: {self.size}\nName: {self.name}\nPrice: ${self.price:.2f}\n"
    
