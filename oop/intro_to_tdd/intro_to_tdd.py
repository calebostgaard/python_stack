class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
    def print_info(self):
        print(f"{self.name}, {self.category}, ${self.price}")

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
    def sell_product(self, id):
        sold = self.products.pop(id)
        sold.print_info()
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            product.update_price(percent_discount, False)

store1 = Store()
prduct1 = Product()
