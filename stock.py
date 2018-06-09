""" """
import copy

class Stock():

    def __init__(self, initial):
        self.products = copy.deepcopy(initial)

    def resupply(self, product, count):
        if count <= 0:
            raise ValueError('Can resupply only with positive count.')

        self.products[product] = self.products.get(product, 0) + count

    def withdraw(self, product, count):
        if count <= 0:
            raise ValueError('Can withdraw only with positive count.')

        if product not in self.products:
            raise ValueError('Unknow product')

        if self.products[product] < count:
            raise ValueError('Insuficcient number of items in stock.')
        self.products[product] -= count

    def available_items(self):
        items = {}

        for product, count in self.products.items():
            if count > 0:
                items[product] = count
                
        return copy.deepcopy(self.products)

stock = Stock({'apples': 22, 'bananas': 7, 'oranges': 9})

stock.resupply('ananas', 5)
stock.withdraw('apples', 10)
print(stock.available_items())