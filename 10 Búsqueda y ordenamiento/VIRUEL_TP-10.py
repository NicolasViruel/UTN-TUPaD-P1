# Práctico 10: Busqueda y ordenamiento
# Objetivo:
# Comprender y aplicar las estructuras condicionales en la programación,
# desarrollando algoritmos que involucren tomas de decisiones.

import random
import time
# 1) Escribe una función busqueda_lineal(lista, objetivo) que recorra la lista y
# devuelva el índice del elemento si se encuentra, o -1 si no está. Luego, prueba la función con
# la lista [10, 20, 30, 40, 50] y busca el número 30.

# def busqueda_lineal(lista, objetivo):
#     for i in range(len(lista)):
#         if lista[i] == objetivo:
#             return i
#     return -1

# # Prueba con la lista solicitada
# lista = [10, 20, 30, 40, 50]
# print(busqueda_lineal(lista, 30))  # Debe imprimir 2

#########################//////////////------------////////////############################

# 2) Modifica la función de búsqueda lineal para contar cuántas comparaciones realiza antes de
# encontrar el número 50 en [10, 20, 30, 40, 50].

# def busqueda_lineal_contando(lista, objetivo):
#     comparaciones = 0
#     for i in range(len(lista)):
#         comparaciones += 1
#         if lista[i] == objetivo:
#             return comparaciones
#     return comparaciones  # Si no encuentra

# # Prueba
# lista = [10, 20, 30, 40, 50]
# print(busqueda_lineal_contando(lista, 50))  # Debe imprimir 5

#########################//////////////------------////////////############################

# 3) Implementa la función busqueda_binaria(lista, objetivo), que tome una lista ordenada y
# devuelva el índice del elemento encontrado o -1 si no está. Luego, pruébala con la lista [1, 3, 5,
# 7, 9, 11, 13, 15] para buscar el número 7.

# def busqueda_binaria(lista, objetivo):
#     inicio = 0
#     fin = len(lista) - 1
#     while inicio <= fin:
#         medio = (inicio + fin) // 2
#         if lista[medio] == objetivo:
#             return medio
#         elif lista[medio] < objetivo:
#             inicio = medio + 1
#         else:
#             fin = medio - 1
#     return -1  # Si no se encuentra


# lista = [1, 3, 5, 7, 9, 11, 13, 15]
# print(busqueda_binaria(lista, 7))  # Debe imprimir 3

#########################//////////////------------////////////############################

# 4) Modifica la búsqueda binaria para contar cuántos pasos se necesitan para encontrar el
# número
# 11 en [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21].

# def busqueda_binaria_contando(lista, objetivo):
#     inicio = 0
#     fin = len(lista) - 1
#     pasos = 0
#     while inicio <= fin:
#         pasos += 1
#         medio = (inicio + fin) // 2
#         if lista[medio] == objetivo:
#             return pasos
#         elif lista[medio] < objetivo:
#             inicio = medio + 1
#         else:
#             fin = medio - 1
#     return pasos  # Si no se encuentra, devuelve los pasos que agarro

# # Prueba
# lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
# print(busqueda_binaria_contando(lista, 11))  # Debe imprimir la cantidad de pasos

#########################//////////////------------////////////############################

# 5) Genera una lista de 20 números aleatorios entre 1 y 100. Luego, implementa una búsqueda
# lineal que intente encontrar el número 50 en la lista generada.

# lista = [random.randint(1, 100) for _ in range(20)]
# print("Lista aleatoria:", lista)

# def busqueda_lineal(lista, objetivo):
#     for i in range(len(lista)):
#         if lista[i] == objetivo:
#             return i
#     return -1

# print("Índice del 50 (lineal):", busqueda_lineal(lista, 50))

#########################//////////////------------////////////############################
# 6) Usa sorted() para ordenar la lista generada en el ejercicio anterior y luego busca el número
# 50 usando búsqueda binaria.
# lista_ordenada = sorted(lista)
# print(lista_ordenada)

# lista = [random.randint(1, 100) for _ in range(20)]
# lista_ordenada = sorted(lista)

# print("Lista ordenada:", lista_ordenada)

# def busqueda_binaria(lista, objetivo):
#     inicio = 0
#     fin = len(lista) - 1
#     while inicio <= fin:
#         medio = (inicio + fin) // 2
#         if lista[medio] == objetivo:
#             return medio
#         elif lista[medio] < objetivo:
#             inicio = medio + 1
#         else:
#             fin = medio - 1
#     return -1

# print("Índice del 50 (binaria):", busqueda_binaria(lista_ordenada, 50))

#########################//////////////------------////////////############################

# 7) Escribe una función que cuente cuántas veces aparece el número 5 en la lista [1, 5, 2, 5, 3,
# 5, 4, 5].

# def contar_ocurrencias(lista, numero):
#     return lista.count(numero)

# lista = [1, 5, 2, 5, 3, 5, 4, 5]
# print(contar_ocurrencias(lista, 5))  # Debe imprimir 4

#########################//////////////------------////////////############################

# 8)Genera una lista ordenada de 10,000 números y mide el tiempo que tarda la búsqueda
# lineal y la búsqueda binaria en encontrar un número. Usa time.time() para medir el
# tiempo.

# lista_grande = list(range(10000))

# # Busqueda lineal
# def busqueda_lineal(lista, objetivo):
#     for i in range(len(lista)):
#         if lista[i] == objetivo:
#             return i
#     return -1

# # Busqueda binaria (misma de antes)
# def busqueda_binaria(lista, objetivo):
#     inicio = 0
#     fin = len(lista) - 1
#     while inicio <= fin:
#         medio = (inicio + fin) // 2
#         if lista[medio] == objetivo:
#             return medio
#         elif lista[medio] < objetivo:
#             inicio = medio + 1
#         else:
#             fin = medio - 1
#     return -1

# # Medir tiempo busqueda lineal
# inicio = time.time()
# busqueda_lineal(lista_grande, 9999)
# tiempo_lineal = time.time() - inicio

# # Medir tiempo busqueda binaria
# inicio = time.time()
# busqueda_binaria(lista_grande, 9999)
# tiempo_binaria = time.time() - inicio

# print(f"Tiempo busqueda lineal: {tiempo_lineal:.6f} segundos")
# print(f"Tiempo busqueda binaria: {tiempo_binaria:.6f} segundos")

#########################//////////////------------////////////############################

# 9) Los diccionarios en Python permiten búsquedas eficientes. Crea un diccionario con
# nombres como claves y edades como valores. Luego, escribe una función que busque una
# edad dada y devuelva el nombre asociado.

# personas = {"Alice": 25, "Bob": 30, "Charlie": 22}

# def buscar_por_edad(diccionario, edad):
#     for nombre, valor in diccionario.items():
#         if valor == edad:
#             return nombre
#     return None

# print(buscar_por_edad(personas, 30))  # Debe imprimir "Bob"









