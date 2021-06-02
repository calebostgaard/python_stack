class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def make_deposit(self, amount):
    	self.balance += amount
    def make_withdrawal(self, amount):
        self.balance -= amount
    def display_user_balance(self):
        print(f"{self.name}: ${self.balance}")
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount

caleb = User("Caleb Ostgaard", 100)
merton = User("Merton Myers", 100)
bailey = User("Bailey West", 200)
zack = User("Zack Springer", 300)

caleb.make_deposit(40)
caleb.make_deposit(90)
caleb.make_deposit(20)
caleb.make_withdrawal(20)

merton.make_deposit(90)
merton.make_deposit(20)
merton.make_withdrawal(10)
merton.make_withdrawal(70)

bailey.make_deposit(150)
bailey.make_withdrawal(10)
bailey.make_withdrawal(15)
bailey.make_withdrawal(5)

caleb.display_user_balance()
merton.display_user_balance()
bailey.display_user_balance()

caleb.transfer_money(merton, 20)
caleb.display_user_balance()
merton.display_user_balance()
