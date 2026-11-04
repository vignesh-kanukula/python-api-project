from helpers import fetch_all
class Product:
    def __init__(self, title, price, stock):
        self.title = title
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product({self.title}, {self.price}, stock={self.stock})"

    def is_low_stock(self):
        return self.stock < 10

    def stock_value(self):
        return self.stock * self.price

    def by_value(product):
        return product.stock_value()
    
    
raw = fetch_all('https://dummyjson.com/products', 'products', 100)
products = [Product(p['title'], p['price'], p['stock']) for p in raw]

# low = [p for p in products if p.is_low_stock()]
# print(len(products), len(low))
# print(sum(p.stock_value() for p in products))
# print(products[0])
# print(low[:3])
def by_value(product):
        return product.stock_value()
top3 = sorted(products, key=by_value, reverse=True)[:3]
for p in top3:
    print(p, f'{p.stock_value():.2f}')