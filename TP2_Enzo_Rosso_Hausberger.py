import math

#1
anios = int(input("Ingrese los anio de su computadora: "))

if anios < 2:
    print("Su computador es nuevo")
else:
    print("Su computador es viejo")

#2
anios = int(input("Ingrese los anio de su computadora: "))

if anios < 0:
    print("El numero es negativo")
else:
    if anios < 2:
        print("Su computador es nuevo")
    else:
        print("Su computador es viejo")

#3
nombre1 , nombre2 = input("Ingrese el primer nombre "), input("Ingrese otro nombre ")

if nombre1[0] == nombre2[0]:
    print("Comienzan con la misma letra")
else:
    print("No comienzan con la misma letra")

#4
lista_partidos = {"A": "rojo", "B": "verde", "C": "Azul"}
voto = input("Ingrese el candidato a votar A, B, o C ").upper().strip()

if voto in lista_partidos.keys():
    print(f"Usted voto a el candidato {voto} por el partido {lista_partidos[voto]}")
else:
    print("Voto no valido")

#5
caracter = input("Ingrese un caracter: ").lower().strip()

if len(caracter) > 1:
    print("Usted ingresó una cadena no un caracter")
else:
    if caracter in ["a", "e", "i", "o", "u"]:
        print("Es una vocal")
    else:
        print(f"{caracter} no es una vocal")

#6
anio = int(input("Ingrese un anio: "))

if (anio % 4 == 0) and (anio % 100 != 0) and (anio % 400 != 0):
    print(f"{anio} es un anio bisiesto")
else:
    print(f"{anio} no es un anio bisiesto")

#7
lista_num = [
    float(input("Ingrese el primer número: ")),
    float(input("Ingrese el segundo número: ")),
    float(input("Ingrese el terer número: ")),
]

print(f"{min(lista_num)} es el menor de los numeros ingresados.")

#8
lista_usuario_pass = [
    input("Ingrese nombre de usuario: ").strip(),
    input("Ingrese el password: ").lower().strip(),
]

if (lista_usuario_pass[0] == "Gwenevere") and (lista_usuario_pass[1] == "excalibur"):
    print("Usuario y contrasenia correctos.\nPuede ingresar a Camelot")
else:
    print("Acceso denegado")

#9
nombre = ord(input("Ingrese su nombre: ")[0].lower().strip())
sexo = ord(input("Ingrese su sexo: ")[0].lower().strip())

if(nombre >= ord("a")) and (nombre <= ord('m')) and ((sexo == ord('f')) or (sexo == ord('m'))):
    print("Grupo A")
else:
    if(nombre > ord('m') and nombre <= ord('z')):
        print("Grupo B")

#10
edad = int(input("Ingrese la edad: "))

if edad < 4:
    print("Entra gratis")
else:
    if edad >= 4 and edad <= 18:
        print("Paga $500")
    else:
        if edad >= 18:
            print("Paga $1000")
        else:
            print("Numero no válido")

#11
tipo_pizza = input("Quiere pizza vegana? s/n ").lower().strip()
ingrediente_v = ["pimiento", "tofu"]
ingrediente_no_v = ["peperoni", "jamón", "salmon"]

def seleccionar_ingrediente(lista_de_ingredientes):
    num = int(input(f"Ingrese el ingrediente: 1-{len(lista_de_ingredientes)} "))
    return lista_de_ingredientes[num - 1]

if(tipo_pizza == "s"):
    print("Ingredientes: ", ingrediente_v)
    print(f"Pizza Vegetariana \nIngredientes: queso mozzarella, tomate y {seleccionar_ingrediente(ingrediente_v)}")
else:
    print("Ingredientes: ", ingrediente_no_v)
    print(f"Pizza comun: \nIngredientes: queso mozzarella, tomate y {seleccionar_ingrediente(ingrediente_no_v)}")

#12
anio_actual = int(input("Ingrese el anio actual: "))
anio_cualquiera = int(input("Ingrese un anio cualquiera: "))

if anio_actual > anio_cualquiera:
    print(f"Pasaron {anio_actual - anio_cualquiera} anios")

if anio_actual < anio_cualquiera:
    print(f"Faltan {anio_cualquiera - anio_actual} para llegar")

#13
num1 , num2 = int(input("Ingrese el primer numero: ")), int(input("Ingrese el segundo numero: "))
mayor = max(num1, num2)
menor = min(num1, num2)

if(mayor < 0 and menor <0) or (mayor == None and menor == None):
    print("Se ingreso un negativo o dato nulo")
else:
    if(mayor % menor == 0):
        print(f"{mayor} es múltiplo de {menor}")

#14
a , b = float(input("Ingresar el coeficiente a: ")) , float(input("Ingresar el coeficiente b: "))

if a == 0:
    if b == 0:
        print("Todos los números son una solucion")
    else:
        print("No tiene solución")
else:
    x = (-b)/a
    print(f"Solución: \n{a}x + {b} = 0 \nx= {round(x, 1)}")

#15
figura = input("Calcular el area \n1 Triangulo 2 Circulo: t/c ").lower().strip()

if(figura == "t"):
    base = int(input("Ingrese la base del triángulo: "))
    altura = int(input("Ingrese la altura: "))
    area = (base * altura) / 2
    print("Area del triánglo: ", round(area, 1))
else:
    if(figura == "c"):
        radio = int(input("Ingrese el radio: "))
        area = math.pi * (radio**2)
        print("Area del círculo: ", round(area , 1))

#16
valor1 , valor2 = int(input("Ingrese el primer valor: ")) , int(input("Ingrese el segundo valor: "))
operacion = int(input("Ingrese la operacion: 1) + 2) * 3) - 4) /  "))

if(operacion == 1):
    print(f"{valor1} + {valor2} = {valor1 + valor2}")
else:
    if(operacion == 2):
        print(f"{valor1} * {valor2} = {valor1 * valor2}")
    else:
        if(operacion == 3):
            print(f"{valor1} - {valor2} = {valor1 - valor2}")
        else:
            if(operacion == 4):
                print(f"{valor1} / {valor2} = {valor1 / valor2}")

#17
dia = input("Ingrese el día: ").lower().strip()
mensajes_por_dia = {
    "lunes" : "Buen comienzo!",
    "viernes" : "Buen finde!",
    "sabado" : "Hoy se sale!",
    "domingo" : "Hoy se duerme"
}

if(dia in mensajes_por_dia.keys()):
    print(mensajes_por_dia[dia])
else:
    print(f"{dia} casi viernes! No queda nada!")

#18
horas_trabajas = int(input("Ingrese las horas trabajadas en el mes: "))
salario_por_hora = float(input("Ingrese el salario por hora: "))
horas_extras = horas_trabajas - 48
salario_sin_extras = salario_por_hora * (horas_trabajas - horas_extras)
salario_horas_extras = (((salario_por_hora * 0.1) + salario_por_hora) * horas_extras) 
salario_total =  salario_sin_extras +  salario_horas_extras

print(f"Horas totales: {horas_trabajas} Horas extras: {horas_extras} \nSalario total: {salario_total}")

#19
cantidad_de_lapices = int(input("Ingrese la cantidad de lápices: "))

if(cantidad_de_lapices >= 1000):
    lapiz_con_descuento = 60 - (60 * 0.7)
    print(f"Costo total: ${lapiz_con_descuento * cantidad_de_lapices}" )
else:
    if(cantidad_de_lapices > 0 and cantidad_de_lapices < 1000):
        print(f"Costo total: ${cantidad_de_lapices * 60}")

#20
notas = []
suma = 0
for num in range(1,5):
    notas.append(float(input(f"Ingrese la {num}ª nota ")))
    suma += notas[num - 1]

promedio = round(suma / len(notas), 0)
print(f"Lista de notas: {notas} \nPromedio: {promedio}")

if(promedio >= 6):
    print("Aprueba")
else:
    if(promedio < 6):
        print("Reprueba")