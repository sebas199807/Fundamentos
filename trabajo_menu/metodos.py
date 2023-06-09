"""
Nombre: Ariel Villa
Curso: Big Data
"""


###CURSO DE FUNDAMENTOS DE PYTHON
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.

#1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero positivo y, 
#  utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada número en la pantalla.


def contador_ascendente (num):
    cont = 0
    while cont <= num:
        print(cont)
        cont += 1

#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero positivo y,
#  utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.


def contador_descendente (num):
    cont = num
    while cont >= 0:
        print(cont)
        cont -= 1

#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positivo y, 
# utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese número y lo imprima en la pantalla.

def suma_numeros (num):
    cont = 0
    suma = 0
    while cont <= num:
        cont += 1
        suma += cont
    return suma - (num + 1) 

#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y, 
# utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla. 
# El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.

def factorial (num):
    cont = 1
    mul = 1
    while cont <= num: 
        mul = mul * cont
        cont += 1
    return mul      

#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, 
# y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al número generado,
# el programa debe imprimir "El número que buscas es menor". Si el usuario ingresa un número menor al número generado, 
# el programa debe imprimir "El número que buscas es mayor". Si el usuario adivina el número, el programa debe imprimir 
# "¡Felicitaciones, adivinaste el número!" y terminar.


import random
def adivinar_num (num):
    numero = 0
    while numero != num:
        numero = int(input("Adivine el numero aleatorio: ")) 
        if numero > num:
            print("El numero que buscas es menor")
        elif numero < num:
            print("El numero que buscas en mayor")
        else:
            print("Adivinaste")

#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, 
# cuente la cantidad de vocales que tiene esa cadena. Para simplificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.

def contar_vocales(cadena):
    contador_vocales = 0
    vocales = ['a', 'e', 'i', 'o', 'u']
    indice = 0
    while indice < len(cadena):        
        if cadena[indice] in vocales:
            contador_vocales += 1        
        indice += 1
    return contador_vocales


#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero positivo y, 
# utilizando un bucle while, calcule la suma de todos los números pares desde cero hasta ese número y lo imprima en la pantalla

def numeros_pares(num):
    suma = 0
    i = 0

    while i <= num:
        if i % 2 == 0:
            suma += i
        i += 1
    return print("La suma de todos los números pares desde 0 hasta", num, "es:", suma)

#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros positivos: 
# una base y un exponente. Utilizando un bucle while, calcule la potencia de la base elevada al exponente y lo imprima en la pantalla.

def potencia (numero, exponente):
    resultado = 1
    cont = 1
    while cont <= exponente:
        resultado = resultado * numero
        cont += 1
    return resultado

#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números y, 
# utilizando un bucle while, calcule el promedio de esos números y lo imprima en la pantalla.

def calculo_promedio(numeros):
    for i in range(len(numeros)):
        numeros[i] = int(numeros[i])

    suma = 0
    i = 0
    while i < len(numeros):
        suma += numeros[i]
        i += 1

    promedio = suma / len(numeros)

    print("El promedio de los números ingresados es:", promedio)


#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de texto y, 
# utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena. 
# Para simplificar el problema, puedes considerar que las palabras están separadas por espacios en blanco.
# Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.

"""
def contador_palabras (cadena):
    cadena = cadena.split("")
    return  len(cadena)

"""

def contador_palabras(cadena):
    contador = 0 
    indice = 0
    while indice < len(cadena):
        if cadena[indice] == " ":
            contador += 1
            indice += 1
    print(contador)