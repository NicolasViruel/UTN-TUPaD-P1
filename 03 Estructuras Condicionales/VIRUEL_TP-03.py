from statistics import mode, median, mean
import random

# Actividades

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Es mayor de edad")
# elif edad < 0:
#     print("La edad no puede ser negativa")

#######################///////////////-------------//////////////##########################

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”

# nota = int(input("Ingrese su nota: "))

# if nota >= 6:
#     print("Aprobado")
# elif nota < 0:
#     print("la nota no puede ser negativa")
# else:
#     print("Desaprobado")

#######################///////////////-------------//////////////##########################

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar

# numero = int(input("Ingrese un numero: "))

# if numero % 2 == 0:
#     print("Ha ingresado un numero par")
# else:
#     print("Por favor, ingrese un numero par")

#######################///////////////-------------//////////////##########################

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edad = int(input("Ingrese su edad: "))
# if edad < 12:
#     print("Niño/a")
# elif edad >=12 and edad < 18:
#     print("Adolescente")
# elif edad >= 18 and edad < 30:
#     print("Adulto/a joven")
# else:
#     print("Adulto/a")

#######################///////////////-------------//////////////##########################

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# contraseña = input("Ingrese su contraseña ")

# if len(contraseña) >= 8 and len(contraseña) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#######################///////////////-------------//////////////##########################

#6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# media = mean(numeros_aleatorios)
# mediana = mean(numeros_aleatorios)

# try:
#     moda = mode(numeros_aleatorios)
# except:
#     moda = None

# print("Numeros: ", numeros_aleatorios)
# print(f"Media: {media}")
# print(f"Mediana: {mediana}")
# print(f"Moda: {moda}")

# # Evaluamos el sesgo
# if moda is None:
#     print("No hay una unica moda, por lo tanto no se puede determinar el sesgo.")
# elif media > mediana > moda:
#     print("Sesgo positivo (a la derecha)")
# elif media < mediana < moda:
#     print("Sesgo negativo (a la izquierda)")
# elif media == mediana == moda:
#     print("Sin sesgo")
# else:
#     print("La distribución no cumple con ninguno de los patrones de sesgo definidos.")


#######################///////////////-------------//////////////##########################

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# frase = input("Ingrese una frase o palabra: ")

# if frase[-1].lower() in "aeiou":
#     frase += "!"
#     print(frase)
# else:
#     print(frase)

#######################///////////////-------------//////////////##########################

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input("Ingrese su nombre: ")
# opcion = int(input("Ingrese 1, 2 o 3 dependiendo de la opcion que desea: \n1. Mayusculas\n2. Minusculas\n3. Primera letra mayuscula\n"))

# if nombre and opcion in [1, 2, 3]:
#     if opcion == 1:
#         print(nombre.upper())
#     elif opcion == 2:
#         print(nombre.lower())
#     elif opcion == 3:
#         print(nombre.title())


#######################///////////////-------------//////////////##########################

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# magnitud = float(input("Ingrese la magnitud del terremoto: "))

# if magnitud < 3:
#     print("Muy leve (imperceptible)")
# elif magnitud >= 3 and magnitud < 4:
#     print("Leve (ligeramente perceptible)")
# elif magnitud >= 4 and magnitud < 5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños)")
# elif magnitud >= 5 and magnitud < 6:
#     print("Fuerte (puede causar daños en estructuras debiles)")
# elif magnitud >= 6 and magnitud < 7:
#     print("Muy fuerte (puede causar daños significativos)")
# elif magnitud >= 7:
#     print("Extremo (puede causar graves daños a gran escala)")

#######################///////////////-------------//////////////##########################

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio te encontrás? (N/S): ").strip().upper()
mes = int(input("¿En qué mes del año estamos? (1-12): "))
dia = int(input("¿Qué día del mes es hoy?: "))
fecha = (mes, dia)

if hemisferio not in ["N", "S"]:
    print("Hemisferio no valido. Debe ser 'N' o 'S'.")
else:
    # Definimos rangos de fechas como tupla (inicio, fin)
    estaciones = {
        "N": {
            "Invierno": ((12, 21), (3, 20)),
            "Primavera": ((3, 21), (6, 20)),
            "Verano": ((6, 21), (9, 20)),
            "Otoño": ((9, 21), (12, 20)),
        },
        "S": {
            "Verano": ((12, 21), (3, 20)),
            "Otoño": ((3, 21), (6, 20)),
            "Invierno": ((6, 21), (9, 20)),
            "Primavera": ((9, 21), (12, 20)),
        }
    }

    estacion = None
    for nombre, (inicio, fin) in estaciones[hemisferio].items():
        if inicio <= fecha <= (12, 31) or fecha <= fin:  # Para manejar el salto de año (dic a mar)
            if inicio <= fin:
                if inicio <= fecha <= fin:
                    estacion = nombre
                    break
            else:  # Casos como del 21/dic al 20/mar (salta de diciembre a marzo)
                if fecha >= inicio or fecha <= fin:
                    estacion = nombre
                    break

    if estacion:
        print(f"En el hemisferio {hemisferio}, estas en {estacion}.")
    else:
        print("No se pudo determinar la estacion.")



