import random
import re
#1
def input_numbers():
    lst = []
    while True:
        num = int(input("Please enter a number, 0 to exit: "))
        if num == 0:
            return lst
        lst = delete_first_index(num, lst)
        lst.append(num)

#2
def delete_first_index(number, lst):
    if number in lst:
        lst.remove(number)
        print(f"First index of {number} was deleted")
        return lst
    else:
        print("Can't deletled this number")
        return lst

#3
def add_all_numbers(lst):
    return sum(lst)

#4
def largest_to_smallest(lst, num):
    if num in lst:
        lst.sort(reverse = True)
        first  = lst.index(num)
        l_to_s = lst[first : -1]
        return l_to_s

def iter_print(lst):
    for n in lst:
        print(n, end = " ")
    print()

#5
def num_iterations(lst):
    group = []
    for i in lst:
        r = 0
        for j in lst:
            if i == j:
                r += 1
        group.append((i,r))
    return group

#6
def names_input(lst):
    while True:
        name = input("Enter the student name: x to exit ")
        if name != "x":
            lst.append(name)
        else:
            break

def names_rep(first_lst, second_lst):
    lst = []
    for n in first_lst:
        for m in second_lst:
            if n == m:
                lst.append(n)
    return lst

def non_rep_names(first_lst, second_lst, rep_lst):
    group = set(first_lst + second_lst)
    for n in rep_lst:
        if n in group:
            group.remove(n)
    return list(group)

#7
def char_count(quote, dct):
    for c in quote:
        if c in dct.keys():
            dct[c] += 1
        else:
            dct.update({c : 1})

#8
def results():
    lts = []
    for i in range(0, 10):
        lts.append([])
        for j in range(0, 10):
            if i == j:
                lts[i].append(0)
            else:
                goles = input(f"Enter the goals of team {i+1} vs team {j+1}: ")
                lts[i].append(goles)
    return lts

def team_results(lst):
    for i in range(0, len(lst)):
        victoria = 0
        derrota = 0
        empate = 0
        for j in range(0,len(lst[i])):
            if i == j:
                continue 
            elif lst[i][j] == lst[j][i]:
                empate += 1
            elif lst[i][j] > lst[j][i]:
                victoria += 1
            elif lst[i][j] < lst[j][i]:
                derrota += 1
        print(f"Equipo\t{i+1}: \n\tVictorias:\t{victoria}\n\tEmpates:\t{empate}\n\tDerrotas:\t{derrota}")

def diference_of_goals(lst):
    for i in range(0, len(lst)):
        goals_scored = 0
        opponent_goals = 0
        for j in range(0,len(lst[i])):
            goals_scored += lst[i][j]
            opponent_goals += lst[j][i]
        print(f"Equipo\t{i+1}: \n\tGoals scored:\t\t{goals_scored}\n\tOpponents Goals:\t{opponent_goals}\n\tDiference:\t\t{abs(goals_scored - opponent_goals)}")

def team_points(lst):
    for i in range(0, len(lst)):
        victoria = 0
        derrota = 0
        empate = 0
        for j in range(0,len(lst[i])):
            if i == j:
                continue 
            elif lst[i][j] == lst[j][i]:
                empate += 1
            elif lst[i][j] > lst[j][i]:
                victoria += 3
        print(f"Equipo {i+1}:\t{victoria + empate} pts.")

#9
def game_board():
    deck_of_the_game = [
    "2❤", "3❤", "4❤", "5❤", "6❤", "7❤", "8❤", "9❤", "10❤", "J❤", "Q❤", "K❤", "A❤",
    "2◆", "3◆", "4◆", "5◆", "6◆", "7◆", "8◆", "9◆", "10◆", "J◆", "Q◆", "K◆", "A◆",
    "2♧", "3♧", "4♧", "5♧", "6♧", "7♧", "8♧", "9♧", "10♧", "Ja♧", "Q♧", "K♧", "A♧",
    "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠"
    ]
    game_deck = []
    question = int(input("How many pairs do you want to play with? "))
    for i in range(0, question):
        election = random.choice(deck_of_the_game)
        game_deck.append(election)
        game_deck.append(election)
    return game_deck

def game_core(tbl, prgs):
    while True:
        print("---Find the pairs of cards---")
        choises = [int(input("Choose the position of the first card:")) -1, int(input("Choose the position of the second card: ")) -1]
        if (choises[0] > len(tbl) and choises[0] < 0) or (choises[1] > len(tbl) and choises[1] < 0):
            print("Invalid number, try again")
        elif choises[0] == choises[1]:
            print("Same number, try again")
        elif (tbl[choises[0]] not in prgs) or (tbl[choises[1]] not in prgs):
            print("You already choose that cards")
        elif tbl[choises[0]] != tbl[choises[1]]:
            print(f"Incorrect pair {tbl[choises[0]]} {tbl[choises[0]]}")
        elif tbl[choises[0]] == tbl[choises[0]]:
            print(f"Correct you find the pair {tbl[choises[0]]} {tbl[choises[0]]}")
            prgs.remove(tbl[choises[0]])
            if not prgs:
                print("You win!")
                break

#10
def matrix_maker(f_number, s_number):
    lts = []
    for i in range(0, f_number):
        lts.append([])
        for j in range(0, s_number):
                lts[i].append(random.randint(1,10))
    return lts

def diagonals(mtx):
    first_diagonal = []
    inverse_diagonal = []
    for i in range(0, len(mtx)):
        for j in range(0, len(mtx[i])):
            if i == j:
                first_diagonal.append(mtx[i][j])
            elif i + j == len(mtx)-1:
                inverse_diagonal.append(mtx[i][j])
    return first_diagonal, inverse_diagonal

#11
def currencie_finder(lst):
    while True:
        print("---Menu---")
        name = input("Enter the name of the currencie: 0 to exit ").title()
        if name in lst:
            c_symbol = lst[name]
            print(f"{name} is {c_symbol}")
        elif name == "0":
            print("Good Bye!")
            break
        else:
            print("Currency not found")

# 12 
def user_maker():
    user_info = {
    "name" : (input("Please, enter your name: ")),
    "age" : (int(input("Please, enter your age: "))),
    "address" : (input("Please, enter your addres: ")),
    "phone number" : (int(input("Please, enter your phone number: ")))
    }
    return user_info

#13
def fruit_sell(lst):
    while True:
        name = input("What fruit are you loking for? 0 to exit: ").title()
        if name == "0":
            print("Good Bye!")
            break
        elif name in lst:
            kg = float(input("How many kg?: "))
            print(f"{name}\t${lst[name] * kg}")
        else:
            print("he fruit is not in stock")