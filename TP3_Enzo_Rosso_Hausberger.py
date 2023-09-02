'''#1
input_word = input("Please enter a word: ")
for n in range (0,10):
    print(input_word)'''

'''#2
age = int(input("Please enter your age: "))
for n in range (1, age+1):
    print("Birthday: ", n)'''

'''#3
number = abs(int(input("Please enter a positive integer number: ")))
for n in range(1, number, 2):
    print(n) if(n == number - 1) else print(n, end= ", ")'''

'''#4
number = abs(int(input("Please enter a positive integer number: ")))
for n in range(number, -1,-1):
    print(n) if(n == 0) else print(n, end= ", ")'''

'''#5
investment = float(input("Please enter the amount of money to invest: "))
anual_interest = float(input("Please enter the anual interest: "))
years = int(input("Please enter the amount of years: "))
interest_rate = anual_interest / 100
for n in range(1, years + 1):
    capital = investment * (1 + interest_rate)** n
    print(f"Year:\t{n}\nProfit:\t{round(capital,2)}")'''

'''#6
number = int(input("Please enter a positive integer number: "))
for i in range(0,number+1):
    for j in range(0,i):
        print("*", end = "")
    print("")'''

'''#7
print("Multiplication Tables")
for i in range(0, 11):
    print("")
    for j in range(0,11):
        print(f"{i}*{j}= {(i*j)}", end = "/ ")'''

'''#8
number = int(input("Please enter a integer number: "))
for i in range(1, number, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")'''

'''#9
password = input("Enter the new password: ").strip()
attempt = ""
while(attempt != password):
    attempt = input("Try to enter the password ")
else:
    print("CORRECT PASSWORD")'''

'''#10
number = int(input("Please enter a integer number: "))
def its_prime(param_number):
    if(param_number <= 1)
        return False
    
    for divisor in range(2, int(param_number**0.5) + 1):
        if param_number % divisor == 0:
            return False
    
    return True

print("It's a prime number") if its_prime(number) else print("It isn't a prime number")'''

'''#11
word = input("Please enter a word: ")[::-1]
for n in word:
    print(n, end = "")'''

'''#12
quote = input("Enter a quote: ")
letter = input("Please enter the letter you want to find: ")
print(f"{letter} is {quote.count(letter)} times.")'''

'''#13
echo = ""
while echo != "exit":
    print(echo)
    echo = input("Echo (Type exit to exit): ")'''

'''#14
num1, num2 = int(input("Please enter an integer number: ")) ,  int(input("Please enter an integer number again: "))
if(num1%2==0 and num2%2==0):
    print(f"{num1} and {num2} are even numbers")
else:
    if(num1%2==0 and num2%2!=0):
        print(f"{num1} is even but {num2} is odd")
    else:
        if(num1%2!=0 and num2%2==0):
            print(f"{num2} is even but {num1} is odd")
        else:
            print(f"{num1} and {num2} are odd numbers")'''

'''#15
number = int(input("Enter a numbre bigger than cero: "))
print("Dividers:", end = " ")
for n in range(1,number+1):
    if(number%n == 0):
        print(n, end =" ")'''

'''#16
number_amount = int(input("Please enter the amount of number you will insert: "))
negative_numbers = 0

for n in range(0, number_amount):
    num = float(input("Enter a number: "))
    if num < 0:
        negative_numbers += 1

print(f"You entered {number_amount} number/s and {negative_numbers} is/are negative")'''

'''#17
import re
frase = input("Enter a frase: ").lower()
vowels = set(re.findall("[aeiou]", frase))
print(vowels)'''

'''#18
fibonacci = [0,1]
print("Fibonacci sequence: ", end = "")
print(0, 1, end=" ")

for n in range(1,10): 
    sum_of_numbers = fibonacci[0]+fibonacci[1]
    print(sum_of_numbers, end=" ")
    fibonacci[0] = fibonacci[1]
    fibonacci[1] = sum_of_numbers'''

'''#19
goal = float(input("Please enter the amount of money you want to save: "))
savings = 0

while True:
        income = float(input("Enter the amount of money: (Positive valies only) "))
        savings += income if income > 0 else print("Please enter a positive number of money")

        if(savings >= goal):
                print(f"Goal:\t{goal}\nCurrent savings:\t{savings}")
                break'''

'''#20
sum_of_numbers, numbers = 0, 1
while numbers != 0:
    numbers = int(input("Enter a number: "))
    sum_of_numbers += numbers

print(sum_of_numbers)'''

'''#21
max_number, number = 0, 1
while number != 0:
    number = int(input("Enter a positive integer number: "))
    if number >= 0:
        if number > max_number:
            max_number = number
    else:
        print("Please enter a positive number")

print("The most bigger number is: ", max_number)'''

'''#22
sum_of_num = 0
even = 0
number = "0"

while int(number) != -1:
    number = input("Enter a positive number (-1 to exit): ")
    
    if int(number) != -1:
        if "-" in number:
            print("Please enter a positive numbers")
        else:
            number_list = list(number)
            for n in range(0, len(number_list)):
                number_list[n] = int(number_list[n])

            sum_of_num = sum(number_list)
            print("Sum: ", sum_of_num)
            if int(number)%2 == 0:
                even += 1

print(even," even numbers have been entered.")'''

'''#23
amount, total = 1, 0
while amount != 0:
    amount = float(input("Enter the cost value (0 to exit): "))
    total += amount

print(f"Total cost: {total}")'''

'''#24
amount, total = 1, 0

while amount != 0:
    amount = float(input("Enter the cost value (0 to exit): "))
    
    if amount < 0:
        print("Please enter a positive value")
    else:
        total += amount

if total > 1000:
    discount = total - (total * 0.1)
    print(f"Total fee:\t{total} whit discount:\t{discount}")
else:
    print(f"Total fee:\t{total}")'''

'''#25
number = int(input("Please enter a positive integer number: "))
multiplication = 1

if number == 0:
    print("Factorial: 0")
else:
    print(f"{number}! =", end=" ")
    for n in range(number, 0, -1):
        print(n, end=" ") if n == 1 else print(n, end=" * ")
        multiplication *= n

print(f" = {multiplication}")'''