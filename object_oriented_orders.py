class costumer():
    def __init__(self, name, money):
        self.name = name 
        self.money = money
        self.basket = []

class product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class basket():
    def __init__(self, number_id, products, costumer):
        self.number_id = number_id
        self.products = products
        costumer.basket = self

    def sum_price(self):
        _price_sum = 0
        for product in self.products:
            _price_sum += product.price
        return _price_sum
    
    def add_to_basket(self, products):
        for product in products:
            self.basket.append(product)


Cristiano_Ronaldo = costumer("cristiano", 9000000)
meat = product("meat", 100)
banana = product("banana", 5)
chicken = product("chicken", 50)
pasta = product("pasta", 25)
Ronaldos_basket = basket(1, [meat, banana, chicken, pasta], Cristiano_Ronaldo)
print(Ronaldos_basket.sum_price())

