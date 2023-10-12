from math import factorial
from TP5F import all_members_info, are_multiple, area, enter_numbers, fac, id_maker, valid_id, last_word, login, maxmin, media_temp, member_info, module, multiples_of_ten, are_multiple, number_frequency, number_frequency_on_group, perimeter, prime_numbers, space, sum_of_digit, times_ten, total_price, words_size

"""#1Corregir los test
idn = int(input("Enter you idn: ").replace(".", "")
print("Correct")if valid_id(idn) else print("Incorrect")"""

"""#2
frase = input("Enter a frase: ").split()
print(last_word(frase))"""

"""#3
members = {}
i = 0
while True:
    full_name = input("Please, enter your full name, nothing to exit: ").split()
    if not full_name:
        break
    
    while True:
        idn = int(input("Please enter your IDN: "))
        if valid_id(idn):
            print("Valid IDN")
            break
        print("Invalid IDN, please try again")
    id_member = id_maker(full_name, idn)
    member_info(full_name, idn, id_member)
    members.update({i : f"ID:\t{id_member}\tIDN:\t{idn}\tFULL_NAME:\t{full_name}\n"})
    i += 1

all_members_info(members)"""

"""#4
num1, num2 = int( input("Enter a number: ")), int(input("Please enter another number: "))
if num2 != 0:
    if are_multiple(num1, num2):
        print(f"{num1} its multiple of {num2}")
    else:
        print(f"{num1} isn't multiple of {num2}")
else:
    print("Wrong input")"""

"""#5
i = 0
days = int(input("Enter the amount of days: "))
while i < days:
    print(f"Day {i+1} Media: {media_temp()}")
    i += 1"""

"""#6
frase = input("Please enter a frase: ")
print(space(frase))"""

"""#7
list_of_numbers = []
while True:
    num = float(input("Plese enter a number, 0 to exit: "))
    if num != 0:
        list_of_numbers.append(num)
    else:
        break
print("MAX: ",maxmin(list_of_numbers)[0],"\nMIN: ", maxmin(list_of_numbers)[1])
"""
"""#8
radius = float(input("Please enter the circle's radius: "))
print("Area: ", area(radius))
print("Perimeter: ", round(perimeter(radius), 1))"""

"""#9
attempts = 0
while attempts < 3:
    username = input("Please enter your user username: ")
    password = input("Please enter your password: ")

    if login(username, password, attempts):
        print("Access granted")
        break
    else:
        attempts += 1
else:
    print("Access denied")"""

"""#10
shopping_cart = {
    "Milk"      :   {"price" : 100, "discount": 0.5},
    "Bread"     :   {"price" : 100, "discount": 0.5},
    "Eggs"      :   {"price" : 100, "discount": 0.5},
    "Apples"    :   {"price" : 100, "discount": 0.5}
}
print(total_price(shopping_cart))"""

"""#11
based_num = [1,2,3,4,5,6,7,8,9,10]
print(multiples_of_ten(based_num, times_ten))"""

"""#12
frase = input("Please enter a frase: ")
print(words_size(frase))
"""
"""#13
vector_x = float(input("Please enter a X: "))
vector_y = float(input("Please enter a Y: "))
vector_z = float(input("Please enter a Z: "))
print(module(vector_x, vector_y, vector_z))"""

"""#14
number = int(input("Please enter an integer number: "))
if prime_numbers(number):
    print(f"The number {number} is prime")
else:
    print(f"The number {number} isn't prime")"""

"""#15
num_register , i = enter_numbers()
fac(num_register)
print(f"Amount of number: {i}")"""

"""#16
number = input("Please enter a number: ")
digit = input("Please enter a digit to search: ")
print(f"{digit} is {number_frequency(number, digit)} on {number}")"""

"""#17 
numbers = []
while True:
    number = int(input("Please enter a prime number: "))
    if prime_numbers(number):
        numbers.append(number)
    else:
        break

print(f"Sum of digits: {sum_of_digit(numbers)}")
number = int(input("Please enter a digit: "))
print(f"The digit is {number_frequency_on_group(numbers, number)} times on {numbers}")
fac([max(numbers)])
"""