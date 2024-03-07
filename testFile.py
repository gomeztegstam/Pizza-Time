from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue, QueueEmptyException





def test_pizza():
    pass
def test_CustomPizza():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    assert cp1.getPrice() == 9.00
    assert cp1.getSize() = "S"
def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPrice() == 12.00
    assert sp1.getSize() = "S"
def test_PizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
    "******\n\
    Order Time: 123000\n\
    CUSTOM PIZZA\n\
    Size: S\n\
    Toppings:\n\
    \t+ extra cheese\n\
    \t+ sausage\n\
    Price: $9.00\n\
    \n\
    ----\n\
    SPECIALTY PIZZA\n\
    Size: S\n\
    Name: Carne-more\n\
    Price: $12.00\n\
    \n\
    ----\n\
    TOTAL ORDER PRICE: $21.00\n\
    ******\n"
def test_OrderQueue():
    order_queue = OrderQueue()

    pizza_order1 = PizzaOrder(90000)
    pizza_order2 = PizzaOrder(93000)

    order_queue.addOrder(pizza_order1)
    order_queue.addOrder(pizza_order2)

    processed_order1 = order_queue.processNextOrder()
    assert "Order Time: 90000" in processed_order1

    processed_order2 = order_queue.processNextOrder()
    assert "Order Time: 93000" in processed_order2
