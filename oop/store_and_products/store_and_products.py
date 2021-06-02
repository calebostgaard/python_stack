class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self
    def print_info(self):
        print(f"{self.name} ({self.category}) - ${self.price:.2f}")
        return self

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
        for product in self.products:
            product.print_info()
        print()
        return self

pet = Store("Pet Store")

chicken_food = Product("chicken", 10, "food")
beef_food = Product("beef", 15, "food")
turkey_food = Product("turkey", 10, "food")
ball_toy = Product("ball", 5, "toy")
bone_toy = Product("bone", 3, "toy")
animal_toy = Product("animal", 6, "toy")
collar_accessory = Product("collar", 15, "accessory")
shoes_accessory = Product("shoes", 25, "accessory")
raincoat_accessory = Product("raincoat", 65, "accessory")


pet.add_product(chicken_food).add_product(beef_food).add_product(turkey_food)
pet.add_product(ball_toy).add_product(bone_toy).add_product(animal_toy).add_product(animal_toy)
pet.add_product(collar_accessory).add_product(shoes_accessory).add_product(raincoat_accessory)

pet.view_products()

pet.sell_product(6)

pet.view_products().inflation(0.05)

pet.view_products().set_clearance("accessory", 0.2)

pet.view_products()

