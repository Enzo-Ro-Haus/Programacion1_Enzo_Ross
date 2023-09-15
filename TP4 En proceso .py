'''#1
x = 0
while  30 >= x:
    x += 1
    if x in [4, 6, 10]:
        print(f"The execution of {x} of x was skipped.")
        continue

    if x == 15: 
        print(f"The execution of the loop was broken when x was {x}.")
        break

    print(f"The value of the loop is: {x}.")'''

'''#2
frase = " "

while True:
    frase = input("Please enter a frase:\t").upper().strip()
    if frase:
        print(frase)
    else:
        break'''


'''#3
menu = 1
bank_op_log = []
bank_account =  0.0

def deposit():
    global bank_account
    global bank_op_log
    num = float(input("Enter the amount of money to be deposited: "))
    if num < 0:
        print("\t\tPositive amounts only")
        return False
    else:
        print(f"\t\tAfter: ${bank_account}")
        bank_account += num
        print(f"\t\tBefore: ${bank_account}")
        bank_op_log.append(f"D {num}")
        return True

def withdrawal():
    global bank_account
    global bank_op_log
    num = float(input("Enter the amount of money to be withdrawn: "))
    if num < 0:
        print("Positive amounts only")
        return False
    else:
        if num > bank_account:
            print("The withdrawal exceeds the avaliable balance in your account")
            return False
        else:
            print(f"After: ${bank_account}")
            bank_account -= num
            print(f"Before: ${bank_account}")
            bank_op_log.append(f"W {num}")
            return True

def banking_transactions(bank_log):
    if bank_log != []:
        for m in bank_log:
            print("\t\t$",m)
    else:
        print("\t\t---NO BANKING TRANSACTIONS---")

while menu != "":
    print("\n<-----Bank Name----->")
    menu = str(input("---Menu---\n1)\tDeposit\n2)\tWithdrawal\n3)\tBanking transactions\n\tExit\n"))
        
    if menu == "1":
        while deposit() == False:
            deposit()
    elif menu == "2":
        while withdrawal() == False:
            withdrawal()
    elif menu == "3":
        banking_transactions(bank_op_log)
    elif menu != "":
        print("\t\tInvalid command, please try again")

print(f"\t\tAccount balance: ${bank_account}")
print("Good bye, thank you for trusting us.")'''


'''#4
num = 1
primes = 0
def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

        return True

while num != 0:
    num = float(input("Enter a number bigger than 1, 0 to exit: "))
    if num < 1:
        print("The number should be bigger than 1")
    else:
        if is_prime(num):
            primes += 1
        
print(f"You enter {primes} prime number/s")'''

'''#5
first_year, second_year = int(input("Enter a year: ")), int(input("Enter another year: "))

for y in range(min(first_year, second_year), max(first_year, second_year), 1):
    if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0) and (y % 10 == 0):
        print(y)
'''

'''#6
for n in range(1, 21):
    if n % 2 != 0:
        continue
    else:
        print(n)'''

'''#7
import random
numbers = []

while len(numbers) <= 10:
    numbers.append(random.randint(1, 10))


print(numbers)
number = int(input("Search a number: "))

for n in numbers:
    if n == number:
        print("Found")
        break
else:
    print("Not found")'''

'''#8
menu = 1
while True:
    menu = int(input("---Menu---\nSelect:\n1)\n2)\n3)\t0)Exit\n"))
    if menu in [0, 1, 2, 3]:
        if menu == 1:
            print("Number 1")
        if menu == 2:
            print("Number 2")
        if menu == 3:
           print("Number 3")
        if menu == 0:
            print("Good bye")
            break
    else:
        print("\t\tInvalid command, please try again")

print("Good bye, thank you for trusting us.")'''