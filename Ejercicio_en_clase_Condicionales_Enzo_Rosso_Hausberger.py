'''Profe la ejecución comienza en la linea 186 '''

'''cronograma_semanal (dic) es una variable global que almacena los días de la semana con sus respectivas clases'''
cronograma_semanal = {
    "lunes": "inicial",
    "martes": "intermedio",
    "miercoles": "avanzado",
    "jueves": "practica hablada",
    "viernes": "ingles",
}

'''meses_del_anio (dic) es una variable global que almacena los meses del anio y la cantidad de días de c/u'''
meses_del_anio = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

'''
Esta función revisa si el string ingresado es un día valido.
Args:
nombre (str): Es el nombre del día
dic_semanal (dic): Es el diccionario donde están los días validos.
Returns: True o un Exception.
'''
def validar_dia(nombre, dic_semanal):
  if nombre in dic_semanal.keys():
    return True
  else:
    raise Exception("Día no valido (nombre)")

'''
Esta función revisa si el entero ingresado es un numero de día valido.
Args:
num_dia (int): Es el numero del día.
Returns: True o un Exception.
'''
def validar_numero_dia(num_dia):
  if (num_dia > 31 or num_dia < 1):
    raise Exception("Número de día no valido")
  else:
    return True

'''
Esta función revisa el entero ingresado es un numero de mes valido.
Args:
mes (int): Es el número del mes.
num_dia (int): Es el número del día
dic_mensual (dic): Es el diccionario donde están los numeros de los meses y su cantidad de días.
Returns: True o un Exception.
'''
def validar_numero_mes(mes, num_dia, dic_mensual):
  if ((mes in dic_mensual.keys()) and (int(dic_mensual[mes]) > num_dia)):
    return True
  else:
    raise Exception(f"Número de mes no valido o el mes nª {mes} no tiene {num_dia} día/s")

'''
Esta función revisa si el string ingresado es una clase valida.
Args:
clase (str): Es el nombre de la clase
dic_semanal (dic): Es el diccionario donde están los días validos.
Returns: True o un Exception.
'''
def validar_clase(clase, dic_semanal):
  if(clase in dic_semanal.values() ):
    return True
  else:
    raise  Exception(f"{clase} no es una clase valida")

'''
Esta función revisa si el dia ingresado coincide con la clase asignada al mismo.
Args:
dia (str): Es el nombre del día
clase (str): Es el nombre de la clase.
dic_semanal (dic): Es el diccionario donde están los días con sus clases validas.
Returns: True o un Exception.
'''
def validar_dia_clase(dia, clase, dic_semanal):
  if dic_semanal[dia] == clase:
      return True
  else:
    raise Exception(f"La clase {clase} no se corresponde con el día {dia}")

'''
Esta función promedia la cantidad de alumnos aprobados.
Returns: porcentaje_aprobados (float)
'''
def promedio_apronbados():
  aprobados = int(input("Cuánto aprobaron: "))
  desaprobados = int(input("Cuántos desaprobaron: "))
  porcentaje_aprobados = round(((aprobados / (aprobados + desaprobados)) * 100), 1)
  return porcentaje_aprobados

'''
Esta función muestra al usuario el estado de la asistencia"
Returns: -
'''
def asistencia():
  presentes = int(input("Ingrese el porcentaje de alumnos presentes sin el %: "))
  if presentes > 50:
    print("Asistió la mayoría")
  else:
    print("No asistió la mayoría")

''''
Esta función crea un dic con los ingresantes como key y sus respectivos aranceles como values.
Returns: alumnos_arancel (dic)
'''
def aranceles_por_alumno():
  alumnos_arancel = {}
  cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
  for num in range(0, cantidad_alumnos):
      alumnos_arancel.update({input("Ingrese el nombre del alumno: ") : float(input("Ingrese el arancel del alumno: $"))})
  print(alumnos_arancel)
  return(alumnos_arancel)

'''
Esta función calcula la suma total de todos los valores enteros de un dic.
Args:
diccionario (dir): Es el diccionario del cual se extraen los valores.
Returns: suma (int)
'''
def arancel_total(diccionario):
  suma = 0
  for value in diccionario.values():
        suma += value
  return suma

'''
Esta función realiza una validación general llamando a las funciones que realizan validaciones particulares.
Guia el curso del programa segun las variables ingresadas.
Llama a las funciones necesarias en cada caso.
Args:
dia (str): Es el nombre del día
mes (int): Es el número del mes.
num_dia (int): Es el número del día
dic_semanal (dic): Es el diccionario donde están los días con sus clases validas.
dic_mensual (dic): Es el diccionario donde están los numeros de los meses y su cantidad de días.
Returns: -.
'''
def validar(dia, num_dia, mes, clase, dic_semanal, dic_mensual):
  
  if(validar_dia(dia, dic_semanal) and validar_numero_dia(int(num_dia)) and validar_numero_mes(int(mes), int(num_dia), dic_mensual) 
    and validar_clase(clase, dic_semanal) and validar_dia_clase(dia, clase, dic_semanal)):
    
    '''Se muestra la fecha respetando el formato'''
    print(f"Fecha: {dia}, {num_dia}/{mes}")

    '''Si es true el usuario deberá ingresar el porcentaje de asistencia a clase y el programa le indicará ‘asistió la mayoría’ 
    en caso de que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así'''
    if(clase == "practica hablada"):
      asistencia()
    else:

      '''Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir 
      ‘Comienzo de nuevo ciclo’ y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por 
      cada alumno, para luego imprimir el ingreso total en $'''
      if(clase == "ingles" and (num_dia == 1 and (mes == 1 or mes == 7))):
        print("Comienzo de un nuevo ciclo")
        print("Arancel total: $", arancel_total(aranceles_por_alumno()))
      else:

        if(clase != "ingles"):

          '''Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los exámenes, pero eso solo si 
          se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen exámenes.'''
          pregunta_examen = input("Se tomo examen? s/n ").lower()

          '''Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el programa le mostrará 
          el porcentaje de aprobados.'''
          if (pregunta_examen == "s"):
            print("Aprobaron el: ", promedio_apronbados(),"%")
          else:
            print("No se tomo examen")

'''<---------------------------------Comienzo de ejecución ----------------------------------------->
Primero se solicita al usuario que ingrese por teclado el día, el número del día, el número del mes y el nombre de la clase.
Dado que los dos últimos datos tienen que ser numéricos son convertidos a enteros. También se eliminan los espacios ingresados por el usuario'''

nombre_dia = input("Ingrese el día de la semana ").lower().strip()
fechas = input("Ingrese la fecha en formato DD/MM: ")
nombre_clase = input("Ingrese el nombre de la clase o nivel: ").strip()

'''Luego se ingresan todas las variables como parámetros a la función validar'''
validar(nombre_dia, fechas[0:2], fechas[3:5], nombre_clase, cronograma_semanal, meses_del_anio)
'''Anuncia el final de la ejecución'''
print("Fin del programa")