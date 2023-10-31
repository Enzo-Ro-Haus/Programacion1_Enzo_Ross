class Contact:
    
    def __init__(self, name = '', phone = '', email = ''):
        self.name = name
        self.phone = phone
        self.email = email
    
    def set_name(self, name):
        self.name = name
    
    def set_phone(self, phone):
        self.phone = phone
    
    def set_email(self, email):
        self.email = email
    
    def info(self):
        return [self.name, self.phone, self.email]
    