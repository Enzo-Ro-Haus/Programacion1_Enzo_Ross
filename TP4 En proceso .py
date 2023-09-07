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

while frase != "":
    frase = input("Please enter a frase:\t").upper().replace(" ", "")
    print(frase)'''

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


while menu != 0:
    print("\n<-----Bank Name----->")
    menu = int(input("---Menu---\n1)\tDeposit\n2)\tWithdrawal\n3)\tAccount balance\n4)\tBanking transactions\n0)\tExit\n"))
    if menu in [0, 1, 2, 3, 4]:
        if menu == 1:
            while deposit() == False:
                deposit()

        if menu == 2:
            while withdrawal() == False:
                withdrawal()

        if menu == 3:
            print(f"\t\tAccount balance: ${bank_account}")
    
        if menu == 4:
            banking_transactions(bank_op_log)
    else:
        print("\t\tInvalid command, please try again")

print("Good bye, thank you for trusting us.")'''

