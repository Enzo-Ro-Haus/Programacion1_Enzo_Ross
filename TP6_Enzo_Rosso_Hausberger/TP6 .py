import random
import re
from TP6F import *
"""
#1 #2 
lst_of_numbers = input_numbers()
iter_print(lst_of_numbers)

#3
print(add_all_numbers(lst_of_numbers))

#4
number = int(input("Please enter a number: "))
iter_print(largest_to_smallest(lst_of_numbers, number))

#5
iter_print(num_iterations(lst_of_numbers))
"""

"""
#6 
students = ([], [])
print("Primary level")
names_input(students[0])
print("Secondary level")
names_input(students[1])
print(f"Primary level: {students[0]}")
print(f"Secondary level: {students[1]}")

repetitive_names = names_rep(students[0], students[1])
non_repetitive_names = non_rep_names(students[0], students[1], repetitive_names)

print(f"Repetitive names: {repetitive_names}")
print(f"Non-repetitive names: {non_repetitive_names}")
"""
"""
#7
i = 1
char_frequency = {}
while i <= 50:
    text = input(f"Please enter the quote nº {i}: ")
    char_count(text, char_frequency)
    i += 1
    
print(char_frequency)
"""
"""
#8
tournament_table = results()

print("Results: ")
for i in tournament_table:
    for j in i:
        print(j, end=" ")
    print()


print("----Teams's results---")
team_results(lst)
diference_of_goals(lst)
team_points(lst)

team_results(tournament_table)
print()
diference_of_goals(tournament_table)
print()
team_points(tournament_table)
"""
"""
#9
board = game_board()
random.shuffle(board)
print(board)
progres = set(board)

game_core(board, progres)
"""
"""
#10
matrix_size = int(input("Plese enter the size x of the matrix: ")), int(input("Plese enter the size y of the matrix: "))
matrix = matrix_maker(matrix_size[1], matrix_size[0])

for i in matrix:
    for j in i:
        print(j, end=" ")
    print()

first_diagonals, inverted_diagonals = diagonals(matrix)
print(f"First: {first_diagonals}")
print(f"Inverse: {inverted_diagonals}")
"""
"""
#11
currencies = {
    "Dollar": "$",
    "Euro": "€",
    "Yen": "¥"
    }

currencie_finder(currencies)
"""
"""
#12
user_info = user_maker()
print(f"{user_info['name']} is {user_info['age']} years old, lives at {user_info['address']} and his/her/their phone number is {user_info['phone number']}")
"""
"""
#13
fruits_kg = {
    "Apple": 1.5,
	"Banana": 0.8,
    "Orange": 1.2,
	"Grapes": 2.5,
	"Strawberries": 3.0
}

fruit_sell(fruits_kg)
"""
