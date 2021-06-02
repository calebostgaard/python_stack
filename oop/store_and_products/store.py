from products import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def sell_product(self, id):
        sold = self.products.pop(id)
        print(f"PURCHASED:")
        sold.print_info()
        print()
        return self
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self
    def view_products(self):
        print(f"'{self.name}' Offered Products:")
        for i in range (len(self.products)):
            self.products[i].print_info()
        print()
        return self

