from contact import Contact

class Agenda:
    
    def __init__(self, contact = Contact):
        self.contact = []
    
    def add_contact(self):
        self.contact.append(Contact())
        self.contact[-1].set_name(input('Enter the contact name: '))
        self.contact[-1].set_phone(input('Enter the contact phone number: '))
        self.contact[-1].set_email(input('Enter the contact email: '))
    
    def show_contact_list(self):
        for i in self.contact:
            print(i.info())
    
    def contact_finder(self, data):
        for i in self.contact:
            if data in i.info():
                return i.info()
    
    def edit_contact(self, data):
        for i in self.contact:
            if data in i.info():
                position = self.contact.index(i)
                
        while True:
            entry = int(input('Edit:\n1.Name\n2.Phone\n3.Email\n0.Exit: '))
            
            if entry == 0:
                print('end of editing')
                break
            elif entry == 1:
                self.contact[position].set_name(input('New name: '))
                print(self.contact_finder(data))
            elif entry == 2:
                self.contact[position].set_phone(input('New phone: '))
                print(self.contact_finder(data))
            elif entry == 3:
                self.contact[position].set_email(input('New email: '))
                print(self.contact_finder(data))
            else:
                print('Invalid input, plese try again')
