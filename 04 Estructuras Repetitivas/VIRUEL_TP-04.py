# Practico Nº 4
import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range(101):
#     print(i)

# ///////////////////////////*************************************///////////////////////////

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 
# numero = input("Ingrese un numero entero: ")
# print(f"El numero tiene {len(numero.strip('-'))} digitos.")

# ///////////////////////////*************************************///////////////////////////

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores. 
# inicio = int(input("Ingrese el primer numero: "))
# fin = int(input("Ingrese el segundo numero: "))

# menor = min(inicio, fin)
# mayor = max(inicio, fin)

# suma = sum(range(menor +1, mayor))
# print(f"La suma de los numeros entre {menor} y {mayor} es: {suma}")

# ///////////////////////////*************************************///////////////////////////

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 
# total = 0
# while True:
#     numero = int(input("Ingrese un numero entero (0 para salir):"))
#     if numero == 0:
#         break
#     total += numero

# print(f"La suma total es: {total}")

# ///////////////////////////*************************************///////////////////////////

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

    # numero_secreto = random.randint(0, 9)
    # intentos = 0

    # while True:
    #     intento = int(input("Adivina el numero (entre 0 y 9): "))
    #     intentos += 1
    #     if intento == numero_secreto:
    #         print(f"Lo adivinaste en {intentos} intentos.")
    #         break
    #     else:
    #         print("Incorrecto, proba de nuevo.")

# ///////////////////////////*************************************///////////////////////////

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente. 
# for i in range(100, -1, -2):
#     print(i)

# ///////////////////////////*************************************///////////////////////////

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario. 
# n = int(input("Ingrese un numero entero positivo: "))
# suma = sum(range(n + 1))
# print(f"La suma de los numeros entre 0 y {n} es: {suma}")
