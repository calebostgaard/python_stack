from products import Product
from store import Store


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