# Resolucion de problemas Analisis de algoritmos

# Objetivo: Determinar la complejidad temporal de diferentes algoritmos
# utilizando la notación Big-O. Comparar distintas soluciones para un mismo
# problema y analizar cuál es más eficiente. 

# Instrucciones: 
# 1. Analiza cada algoritmo y determina su orden de complejidad T(n) y O(n).
# 2. Justifica tu respuesta indicando los pasos relevantes en el análisis.
# 3. En los ejercicios 1 y 2, compara ambas soluciones y argumenta cuál es
# más eficiente. 

# Ejercicio 1: Suma de los primeros n números  

# Analisis:

# El bucle for se ejecuta n veces.

# En cada iteracion se realiza una suma y una asignacion → operaciones constantes.

# T(n): n operaciones
# O(n): Lineal

#########################//////////////------------////////////############################

# Ejercicio 2: Suma de los primeros n numeros 

# Análisis:

# Realiza una sola operacion matematica, sin bucles ni recursion, no importa el tamaño de n.

# T(n): 1
# O(1): Constante

# Comparación: La solución del Ejercicio 2 es más eficiente que la del Ejercicio 1,
# ya que ejecuta una única operación en lugar de recorrer todos los números. 

#########################//////////////------------////////////############################

# Ejercicio 3: Búsqueda de un elemento en una lista desordenada 

# Analisis:

# En el mejor caso, el elemento es el primero → 1 operacion.

# En el peor caso, el elemento esta al final o no esta → n iteraciones.

# T(n) peor caso: n
# O(n): Lineal

#########################//////////////------------////////////############################

# Ejercicio 4: Encontrar el número máximo en una lista 

# Analisis:

# Recorre toda la lista una vez.

# Comparaciones simples y actualizaciones de valor.

# T(n): n
# O(n): Lineal

#########################//////////////------------////////////############################

# Ejercicio 5: Ordenamiento por selección 

# El primer for itera n veces.
# El segundo for realiza aproximadamente n/2 iteraciones en promedio en cada
# ciclo.
# Esto da lugar a una complejidad de O(n^2). 
#  Complejidad temporal: O(n^2) 
# Conclusion: Es un algoritmo poco eficiente para grandes volumenes de datos.
# Algoritmos como QuickSort O(n log n) son preferibles para ordenar listas
# grandes. 

#########################//////////////------------////////////############################

# Conclusion Final: 
# • Los algoritmos eficientes reducen la cantidad de operaciones necesarias. 
# • La busqueda secuencial y la busqueda del maximo tienen O(n), lo que es
# aceptable para listas pequeñas. 
# • Para ordenar datos, es importante elegir algoritmos mas rapidos como
# QuickSort o MergeSort. 