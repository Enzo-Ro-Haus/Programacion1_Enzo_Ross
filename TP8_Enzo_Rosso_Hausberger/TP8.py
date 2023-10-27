"""#1
def cant_digits(n):
    cant = 0
    if n < 10:
        cant += 1
        return cant
    else:
        rest = n // 10
        return 1 + cant_digits(rest)

print(cant_digits(12345))
print(cant_digits(123456))
print(cant_digits(1234567))"""

"""#2 Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.

def is_power(n1, n2, p):
    potencia = p
    if pow(n1, p) == n2 :
        potencia += 1
        return potencia
    else:
        return  is_power(n1, n2, p + 1)

print(is_power(2, 8, 1))"""

"""#3
def concurrency(a, b):
    i = a.find(b, 0)
    if i == -1:
        return []
    else:
        return [i] + concurrency(a.replace(b, " " * len(b), 1), b)

    
quote = "Un tete a tete con Tete"
print(f"Posiciones: {concurrency(quote, 'te')}")"""

"""#4
def even(n):
    if n == 0:
        return "even"
    else:
        return odd(n-1)

def odd(n):
    if n == 0:
        return "odd"
    else:
        return even(n -1)

print(even(4))
print(even(3))"""

"""#5
def max_num(lst, i = 0):
    if lst[i] > lst[i+1]:
        max_value = lst[i]
        return max_value
    else:
        return max_num(lst, i+1)

numbers = [8,90,100,3,5,6,7,9]
print(f"Max number: {max_num(numbers)}")"""

#6
"""def repetition(lst, i, back= []):
    if i <= 0:
        return sorted(back)
    for number in lst:
        back.append(number)
    return repetition(lst, i - 1, back)

rep = ([1,3,3,7],2)
print(repetition(rep[0], rep[1]))"""

"""#7
def summation(n, p):
    if n == 2:
        return  2 * p
    else:
        return n * p + summation(n-1, p)

n, p = int(input("Enter n: ")), int(input("Enter p: "))
print(summation(n, p))"""

#8 Triangulo de Pascal
"""
def pascal_triangle(n):
    if n == 0:
        return []
    if n == 1:
        print([1])
        return [1]
    else:
        new_row = [1]
        last_row = pascal_triangle(n-1)
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
    print(new_row)
    return new_row

pascal_triangle(5)
"""
"""#9
def combinations(lst, n, pf = ""):
    if n == 0:
        print(pf)
        return
    for c in lst:
        combinations(lst, n-1, pf + c)

unique_char = ['a','b','c','d','e']
num = 4
combinations(unique_char, num)"""

"""#10
def paper_size(n, base = {"width" : 841, "height": 1189}):
    if n == 0:
        return base
    else:
        return paper_size(n - 1,  base = {"width" : base['height']//2, "height": base['width']})

for i in range(0,11):
    sizes = paper_size(i)
    print(f"A{i}: {str(sizes['width'])} x {str(sizes['height'])} mm")"""