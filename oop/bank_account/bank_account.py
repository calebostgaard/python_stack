class BankAccount:
    def __init__(self, int_rate= 0.05, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else: 
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if(self.balance > 0):
            self.balance *= (self.int_rate + 1)
        return self

account1 = BankAccount(0.15, 450)
account2 = BankAccount(0.1, 350)

account1.deposit(40).deposit(90).deposit(120).withdraw(60).yield_interest().display_account_info()
account2.deposit(24).deposit(45).withdraw(15).withdraw(5).withdraw(25).withdraw(35).yield_interest().display_account_info()
