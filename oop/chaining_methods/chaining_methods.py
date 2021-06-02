class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print(f"{self.name}: ${self.balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self

caleb = User("Caleb Ostgaard", 100)
merton = User("Merton Myers", 100)
bailey = User("Bailey West", 200)
zack = User("Zack Springer", 300)

caleb.make_deposit(40).make_deposit(90).make_deposit(20).make_withdrawal(20).transfer_money(merton, 20).display_user_balance()
merton.make_deposit(90).make_deposit(20).make_withdrawal(10).make_withdrawal(70).display_user_balance()
bailey.make_deposit(150).make_withdrawal(10).make_withdrawal(15).make_withdrawal(5).display_user_balance()
