import time  # Importamos la libreria que permite hacer pausas de tiempo

# Mostramos un mensaje inicial
print("Contador binario del 0 al 15:")

# Usamos un bucle para contar del 0 al 15
# for numero in range(16):  # range(16) va del 0 al 15 inclusive
#     binario = format(numero, '04b')  # Convertimos el numero a binario de 4 cifras
#     print(f"{numero} en binario es: {binario}")
#     time.sleep(1)  # Esperamos 1 segundo antes de mostrar el siguiente numero

for numero in range(16): # range(16) va del 0 al 15 inclusive
    n = numero
    restos = [] # Lista para guardar los restos de la didivion por 2

    # Si el numero es 0, su binario es directamente 0000
    if numero == 0:
        restos =[0]
    else:
        while n > 0:
            resto = n % 2  # Calculamos el resto de la division por 2
            restos.insert(0, resto) # Lo agregamos al principio de la lista
            n = n // 2 # Division entera por 2

    # Aseguramos que tenga 4 bits rellenando con ceros a la izquierda
    while len(restos) < 4:
        restos.insert(0, 0)
    binario = ''.join(str(bit) for bit in restos) # Convertimos la lista a string

    print(f"{numero} en binario es: {binario}")
    time.sleep(1)  # Esperamos 1 segundo antes de mostrar el siguiente numero



# 💬 Parte 1: Introducción (Persona 1)
# Hola, somos el grupo [Nombre del grupo o integrantes], y este es nuestro trabajo práctico para la materia de programación.
# En este proyecto hicimos una simulación de un contador binario desde el número 0 al 15 utilizando Python.
# Este tipo de contador es común en electrónica digital, donde cada número se representa con 4 bits.

# 💬 Parte 2: Explicación del código (Persona 2)
# Para hacer este programa, primero importamos la librería time, que nos permite usar la función sleep() para hacer una pausa entre cada número, simulando el retardo de un circuito real.

# Después usamos un bucle for para contar del 0 al 15.
# En cada vuelta del bucle, convertimos el número decimal a binario con format(numero, '04b').
# Esto hace que el número binario tenga 4 cifras, como si fuera un contador de 4 LEDs encendidos o apagados.

# 💬 Parte 3: Demostración del programa (Persona 3)
# Ahora les mostramos cómo funciona el programa.
# Al ejecutarlo, se van mostrando los números del 0 al 15 junto a su forma en binario, con una pausa de 1 segundo entre cada uno.

# (Acá mostramos por consola el resultado del programa)

# 💬 Parte 4: Cierre (Última persona)
# Este trabajo nos ayudó a entender cómo funciona un bucle en Python y cómo se pueden representar los números en binario.
# También aprendimos a usar la función sleep() para simular un retardo, como si fuera un circuito digital.
# Esperamos que les haya gustado. ¡Gracias por mirar!