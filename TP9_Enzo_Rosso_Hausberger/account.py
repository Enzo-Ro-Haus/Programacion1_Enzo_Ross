from person import Person

class Account:
    
    def __init__(self, owner, amount = 0.0):
        self.owner = owner
        self.__amount = amount
    
    def set_owner(self, person):
        if isinstance(person, Person):
            self.person = person
        else:
            print('Invalid type, please enter a Person object')
    
    def __set_amount(self, amount):
        if isinstance(amount, float):
            self.__amount = amount
        else:
            print('Invalid type, please enter a float type')
    
    def get_amount(self):
        return self.__amount
    
    def get_owner(self):
        return self.owner
    
    def show(self):
        return f"Owner: \n{self.owner.show()}\nAmount: {self.get_amount()}"
    
    def deposit(self, amt):
        if amt > 0:
            self.__set_amount(self.__amount + amt)
    
    def withdraw(self, amount):
        if amount < self.__amount:
            self.__set_amount(self.__amount - amount)
        else:
            print('Invalid withdraw, the amount entered exceeds the available balance in your account')