class Person:
    
    def __init__(self, name = '', age = None, idn = ''):
        self.name = name
        self.age = age
        self.idn = idn
    
    
    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            print("Invalid type, please enter a string type")
    
    def set_age(self, n):
        if isinstance(n, int):
            self.age = n
        else:
            print("Invalid type, please enter an integer type")
    
    def set_idn(self, idn):
        if isinstance(idn, str):
            self.idn = idn
        else:
            print("Invalid type, please enter an string type")
    
    def name(self):
        return self.name
    
    
    def age(self):
        return self.age
    
    
    def idn(self):
        return self.idn
    
    def show(self):
        return f'Name: {self.name}\nAge: {self.age}\nIDN: {self.idn}'
    
    
    def legal_age(self):
        return True if self.age > 17 else False