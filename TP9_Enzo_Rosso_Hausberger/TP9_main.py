from account import Account
from agenda import Agenda
from person import Person
from triangle import Triangle
"""
#1
adult = Person()

adult.set_name(45)
adult.set_age('27')
adult.set_idn(39377)

adult.set_name('Philip Anthony Hopkins')
adult.set_age(85)
adult.set_idn('65348972')

print(adult.show())s
print("It's over 18"if adult.legal_age() else "It's minor")

minor = Person()

adult.set_name('Roman Griffin Davis')
minor.set_age(16)
adult.set_idn('87223584')

print(minor.show())
print("It's over 18"if minor.legal_age() else "It's minor")
"""
"""
#2
account = Account(adult)
account.deposit(1500.75)
print(account.show())
account.withdraw(2000.0)
account.withdraw(500)
print(f"Your amount: {account.get_amount()}")
"""
"""
#3
triangle_e = Triangle(1,1,1)
triangle_i = Triangle(1,1,2)
triangle_s = Triangle(1,2,3)

print(triangle_e.larger_side())
print(triangle_i.larger_side())
print(triangle_s.larger_side())

print(triangle_e.triangle_type())
print(triangle_i.triangle_type())
print(triangle_s.triangle_type())
"""
"""
#4
agenda = Agenda()

while True:
    menu = int(input('- MENU -\n1.Add new contact\n2.Contacts list\n3.Find contact\n4.Edit contact\n0.Close agenda '))
    
    if menu == 0:
        print('Bye')
        break
    elif menu == 1:
        agenda.add_contact()
    elif menu == 2:
        agenda.show_contact_list()
    elif menu == 3:
        clue = input('Please enter any information about the contact you wish to find: ')
        print(agenda.contact_finder(clue))
    elif menu == 4:
        clue = input('Please enter any information about the contact you wish to edit: ')
        agenda.edit_contact(clue)
    else:
        print('Invalid input, plese try again')
"""
