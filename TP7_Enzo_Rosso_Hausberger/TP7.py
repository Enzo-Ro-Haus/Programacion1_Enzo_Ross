#Trabajo Practico 8
from itertools import count
from OyB_Ejercitacion_en_clase import *

def fill_list(data):
    lst = []
    while True:
        if data == 1:
            while True:
                number = int(input("Please enter a number: 0 to exit\n: "))
                if number!= 0:
                    lst.append(number)
                else:
                    return lst
        elif data == 2:
            while True:
                word = input("Please enter a word/quote: Nothing to exit\n: ")
                if word:
                    lst.append(word)
                else:
                    return lst
        elif data == 3:
            while True:
                book = {
                    "title" : (input("Title: ")),
                    "author" : (input("Author: ")),
                    "year" : (input("Year: ")),
                        }
                if book['title'] != "":
                    lst.append(book)
                else:
                    return lst
        elif data == 0:
            break

"""#1
print("1)")
numbers = fill_list(1)
bubble_sort(numbers)
print(numbers)"""

"""#2
print("2)")
words = fill_list(2)
words = sorted(words)
print(words)"""

"""#3
def library_order(lst):
    while True:
        order = int(input("Select books for: \n1)Title\n2)Author\n3)Year\n0)Exit"))
        if order == 0:
            break
        elif order == 3:
            lst = sorted(lst, key = lambda x: x['year'])
            return lst
        elif order == 2:
            lst = sorted(lst, key = lambda x: x['author'])
            return lst
        elif order == 1:
            lst = sorted(lst, key = lambda x: x['title'])
            return lst

print("3)")
library = fill_list(3)
library = library_order(library)
print(library)
"""
"""#4
print("4)")
quotes = fill_list(2)
print(quotes)
quotes = sorted(quotes, key=lambda x: len(x))
print(quotes)"""

"""#5
print("5)")
quotes = fill_list()
print(quotes)
quotes = sorted(quotes, key=lambda x: len(x), reverse=True)
print(quotes)"""


"""print("6)")
numbers = fill_list(1)
print(numbers)
numbers = counting_sort(numbers)
print(numbers)"""

"""#7
print("7)")
numbers_and_words = fill_list(2)
print(numbers_and_words)
numbers_and_words = sorted(numbers_and_words)
print(numbers_and_words)"""

#8
"""
print("8)")
numbers = fill_list(1)
print(numbers)
merge_sort(numbers)
print(numbers)"""