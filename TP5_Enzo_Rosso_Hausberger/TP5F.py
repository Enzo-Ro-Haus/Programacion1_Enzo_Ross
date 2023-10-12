import math
import re

#This function checks if the given document number is valid. It returns True if the document number is valid and False otherwise.
def valid_id(document):
    if type(document) == int:
        return document > 999_999 and document < 100_000_000
    else:
        print("Wrong type of input")
        return False


#This function returns the last word of the given quote.
def last_word(quote):
    if type(quote) == list:
        return str(quote[(len(quote)-1)])
    else:
        print("Wrong type of input")
        return ""

#This function returns the first word of the given quote.
def first_word(quote):
    if type(quote) == list:
        return str(quote[0])
    else:
        print("Wrong type of input")
        return ""

#This function creates a unique ID for each member. It takes the first name, last name, and ID number as input and returns the unique ID.
def id_maker(f_name, id_number):
    if first_word(f_name) != "" and valid_id(id_number):
        return str(f_name[0]) + str(len(f_name[-1])) + str(id_number)[0:3]
    else:
        print("Wrong input type")
        return ""

#This function prints the information of a member. It takes the first name, ID number, and unique ID as input.
def member_info(f_name, id_number, id_client):
    print(f"Name:\t{f_name}")
    print(f"IDN:\t{id_number}")
    print(f"ID:\t{id_client}")

#This function prints the information of all the members in the list. It takes the list of members as input.
def all_members_info(members_dty):
    print("\t\t\t--- MEMBERS ---")
    for m in range(0, len(members_dty)):
        print(members_dty[m])

# This function checks if 'number' is a multiple of 'a_number' and prints the result.
def are_multiple(number, a_number):
    if type(number) == int and type(a_number) == int:
        return number % a_number == 0
    else:
        print("Wrong input type")

# This function calculates the average temperature for a given number of days.
def media_temp():
        max = float(input("Please enter the max temperature: "))
        min = float(input("Please enter the min temperature: "))
        if type(max) == float and type(min) == float:
            media = (max + min)/2
            return media
        else:
            print("Wrong input type")

# This function removes extra spaces from a string.
def space(f):
    if type(f) == str:
        return re.sub(r'\s+', ' ', ' '.join(f))
    else:
        print("Wrong input type")

# This function calculates the maximum and minimum values in a list of numbers.
def maxmin(l_num):
    return max(l_num), min(l_num)

# This function calculates the area of a circle with radius 'r'.
def area(r):
    return round(((math.pi) * (r)**2),1)

# This function calculates the perimeter of a circle with radius 'r'.
def perimeter(r):
    return round((2 * (math.pi) * r), 1)

# This function validates a user's login credentials.
def login(name, pass_w, trys):
    if name == "usuario1":
        if pass_w == "asdasd":
            print("Correct")
            return True
        else:
            print("Wrong Password")
            print("Attempts: ", (2 - trys))
            return False
    else:
        print("Wrong user username")
        print("Attempts: ", (2 - trys))
        return False

# This function calculates the total price of a list of items with discounts.
def total_price(purchase_information):
    final_price = 0
    for p in purchase_information.values():
        final_price += p["price"] * p["discount"] 
    return final_price

# This function multiplies a number by 10.
def times_ten(number):
    return number * 10

# This function applies a function to each element in a list of numbers.
def multiples_of_ten(numbers, function):
    for i in range(0, len(numbers), 1):
        numbers[i] = function(numbers[i])

    return numbers

# This function calculates the length of each word in a string and returns a dictionary.
def words_size(f):
    words_length = {}
    edited_frase = f.split()
    
    for j in range(0,len(edited_frase)):
        words_length.update({edited_frase[j] : len(edited_frase[j])})
    
    return words_length

# This function calculates the magnitude of a 3D vector.
def module(vx, vy, vz):
    return round(math.sqrt(pow(vx, 2) + pow(vy, 2) + pow(vz, 2)), 1)

# This function checks if a number is prime.
def prime_numbers(num):
    if num%num != 0:
        return False
    else:
        for n in range(2, num):
            if num % n == 0:
                return False
        else:
            return True

# This function calculates the factorial of a list of numbers.
def fac(ln):
    for i in ln:
        f = 1
        print(f"{round(i)}! = ", end="")
        for j in range(1 , (int(i) + 1)):
            f *= j
            print(f"{j}", end=" ")
    
        print(f" = {f}", end="\n")

# This function reads numbers from the user until 0 is entered and returns them as a list.
def enter_numbers():
    numbers = []
    i = 0
    while True:
        num = float(input("Please enter a number, 0 to exit: "))
        if num == 0:
            break
        else:
            i += 1
            numbers.append(num)
    
    return numbers, i

# This function counts the frequency of a digit in a number.
def number_frequency(num, dig):
    i = 0
    for d in num:
        if d == dig:
            i += 1
    
    return i

# This function reads prime numbers from the user until a non-prime number is entered.
#def input_prime_numbers(array_of_numbers):


# This function calculates the sum of the digits in a list of numbers.
def sum_of_digit(a_of_num):
    answers = []
    for n in a_of_num:
        sum = 0
        for l in str(n):
            sum += int(l)
        answers.append(sum)
    return answers

# This function counts the frequency of a digit in a list of numbers.
def number_frequency_on_group(a_of_num, number):
    j = 0
    for t in a_of_num:
        j += number_frequency(str(t), str(number))
    
    return j