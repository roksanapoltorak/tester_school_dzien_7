""" """
import copy
import json

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

    def save(self, file_obj):

        for product, count in self.products.items():
            file_obj.write(product + ',' + str(count) + '\n')

    def save2(self, file_obj):
        lines = [prod + ',' + str(count) + '\n' for prod, count in self.products.items()]
        file_obj.writelines(lines)

    @staticmethod
    def load(file_object):
        data = {}
        for line in file_object:
            record = line.rstrip('\r\n').split(',')
            data[record[0]] =  int(record[1])
        return Stock(data)

    def to_json(self):
        return json.dumps(self.products)

    @staticmethod
    def from_json(json_str):

        products = json.loads(json_str)

        return Stock(products)

    def to_json_file(self, output_file):
        json.dump(self.products, output_file)

    @staticmethod
    def from_json_file(json_file):
        return Stock(json.load(json_file))


stock = Stock({'apples': 22, 'bananas': 7, 'oranges': 9})

stock.resupply('ananas', 5)
stock.withdraw('apples', 10)
print(stock.available_items())

print(stock.to_json())
stock_json = stock.to_json()
stock2 = Stock.from_json(stock_json)
print(stock2.available_items() == stock.available_items())
print(stock2.products == stock.products)


with open('magazyn.json', 'wt') as stock_json:
    stock.to_json_file(stock_json)

with open('magazyn.json', 'rt') as stock_json:
    stock4 = Stock.from_json_file(stock_json)

print(stock2.products == stock4.products)
