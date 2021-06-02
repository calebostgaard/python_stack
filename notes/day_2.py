


# Default Parameters

class User:
        def __init__(self, name, password, email, age = 0):
            self.name = name
            self.age = age
            self.email = email
            self.balance = amount
            self.password = password
        def print_info(self):
            print(self.name)
            print(self.age)
            print(self.email)
            print(self.balance)
            print(self.password)
user2 = User("John", "qwert12345", "john@gmail.com", 59)

user2.print_info()