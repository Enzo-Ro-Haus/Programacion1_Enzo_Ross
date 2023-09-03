from datetime import *
from cmath import *
import math

#1
base = int(input("Ingrese la  base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))
perimetro = 2 * base + 2 * altura
area = base * altura
print("1)\nperimetro:\t", perimetro
      ,"\narea:\t", area)
print("\n")

#2
cateto1= float(input("2)\nIngrese el tamaño del cateto a: "))**2
cateto2 = float(input("Ingrese el tamaño del cateto b: "))**2
hipotenusa = ((cateto1) + (cateto2))**(1/2)
print("hipotenusa:\t", hipotenusa)
print("\n")

#3
num1 = 25
num2 = 10
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2
print("3)\nsuma:\t", suma
      ,"\nresta:\t", resta
      ,"\nproducto:\t", producto
      ,"\ndivision:\t", division)
print("\n")

#4
fahrenheit = float(input("4)\nIngrese los grados ºF: "))
celsius = round((((fahrenheit - 32) * 5) / 9), 2)   
print(fahrenheit, "ºF equivale a ", celsius, "º C")
print("\n")

#5
#a) nombre = input("¿Cuál es tu cancion favorita? ")
print("5)\na) nombre = input(\"¿Cuál es tu cancion favorita?\")")
#b) precio = float(input("Precio: "))
print("b) precio = float(input(\"Precio: \"))")
#c) edad = int(input(“Edad: “))
# print("print(\"tu edad es \", edad)")
print("c) print(\"tu edad es \", edad)")
#d)d)	edad = int(input(“Edad: “))
#print(“Veamos si tu edad es 18…”, edad=18)
print("d) print(\"Veamos si tu edad es 18…\", edad == 18)")
print("\n")

#6
num1 = len(input("6)\nIngrese el numero 1: ")) 
num2 = len(input("Ingrese el numero 2: ")) 
num3 = len(input("Ingrese el numero 3: ")) 

print("\n6)\nLargo numero 1:\t", num1
      ,"\nLargo numero 2:\t", num2
      ,"\nLargo numero 3:\t", num3
      ,"\nTotal:\t", num1 + num2 + num3
      ,"\nMedia:\t", (num1 + num2 + num3)/3)
print("\n")

#7
minutos = int( input("7)\nIngrese la cantidad de minutos: ") )
print("Corresponde a: ", (minutos // 60)," horas y ", (minutos % 60), " minutos" )
print("\n")

#8
sueldo_base = 50000
comision = sueldo_base * 0.1
dinero_final = sueldo_base + (comision * 3)
print("8)\nObtendra a fin de mes:\t", dinero_final)
print("\n")

#9
total_compra = 100
descuento = total_compra * 0.15
pago_final = total_compra - descuento
print("9)\nMonto original:\t$",total_compra
      ,"\nDescuento:\t$", descuento
      ,"\nPago final:\t$", pago_final)
print("\n")

#10
a = [10, 8, 10]
promedio_calificaciones = sum(a) / len(a)
nota_examen_final = 8
nota_trabajo_final = 8

calificacion_final = (promedio_calificaciones * 0.55) + (nota_examen_final * 0.3) + (nota_trabajo_final * 0.15)
print("10)\nLa calificacion final es:\t", round(calificacion_final, 0))
print("\n")

#11
numero1 = int(input("11)\nIngrese el numero 1: "))
numero2 = int(input("Ingrese el numero 2: "))
distancia = abs(numero1 - numero2)
print("La distancia entre "
      , numero1, " y ", numero2
      , " es de ", distancia)
print("\n")

#12
numero = float(input("12)\nIngrese un numero: "))
raiz_cuadradra = numero**1/2 
raiz_cubica = numero**1/3
print("Numero:\t", numero,
      "\nRaiz cuadrada:\t", raiz_cuadradra,
      "\nRaiz cubica:\t", raiz_cubica)
print("\n")

#13
numero = 35
numero_invertido = int(str(numero)[::-1])
print("13)\nNumero: ", numero," numero invertido: ", numero_invertido)
print("\n")

#14
a = int(input("14)\nIngrese una variable numerica: ")) 
b = int(input("Ingrese una variable numerica: "))
print("Antes del intercambio\na: ",a,
      "\nb: ", b)
a,b = b,a
print("a: ",a,
      "\nb: ", b)
print("\n")

'''#15
tiempo_partida = [
    int(input("Hora de partida: ")),
    int(input("Minutos de partida: ")), 
    int(input("Segundos de partida: "))]

cantidad_segundos = int(input("\nIngrese la cantidad de segundos de A a B: "))

hora = int(tiempo_partida[0] + (cantidad_segundos/60)/60)
minutos = int(tiempo_partida[1] + (cantidad_segundos/60)%60)
segundos = int(tiempo_partida[2] +(cantidad_segundos%60))

if segundos >= 60:
    segundos -= 60
    minutos += 1

if minutos >= 60:
    minutos -= 60
    hora += 1

if hora >= 24:
    hora -= 24

print(f"Hora de llegada a la ciudad B: {hora}:{minutos}:{segundos}")
'''
#16
nombre = input("16)\nIngrese su nombre: ")[0].capitalize
apellido = input("Ingrese su apellido ")[0].capitalize
print("Iniciales: ", nombre, apellido)
print("\n")

#17
usuario = input("17)\nIngrese su nombre: ")
print(f"Ahora estás en la mátrix {usuario}.")
print("\n")

#18
costo_cena = float(input("18)\nIngrese el costo de la cena: "))
servicio  = costo_cena * 0.62
propina = costo_cena * 0.1
costo_total = costo_cena + servicio + propina
print("Cena:\t$", costo_cena,
      "\nServicio:\t$", servicio,
      "\nPropina:\t$", propina,
      "\nCosto total:\t$", round(costo_total, 2))
print("\n")

#19
dia = int(input("19)\nIngrese su dia de nacimiento "))
mes = int(input("Ingrese su mes de acimiento "))
anio = int(input("Ingrese su anio de nacimiento "))
print(f"{dia}/{mes}/{anio}")
print("\n")

#20
fecha = date(int(input("20)\nIngrese su anio de nacimiento ")),
            int(input("Ingrese su mes de acimiento ")),
            int(input("Ingrese su dia de nacimiento "))).strftime("%d/%m/%Y")
print(fecha)
print("\n")

#21
km_por_litro = float(input("21)\nIngrese la cantidad de km por l: "))
capacidad_del_tanque = float(input("Ingrese la capacidad de su tanque en l: "))
km_a_recorrer = float(input("Ingrese la cantidad de km que va a recorrer: "))
combustible_necesario = (km_a_recorrer / km_por_litro) / capacidad_del_tanque
if combustible_necesario > math.trunc(combustible_necesario):
      combustible_necesario +=1 

print(f"Necesita {round(combustible_necesario, 0)} tanques")
