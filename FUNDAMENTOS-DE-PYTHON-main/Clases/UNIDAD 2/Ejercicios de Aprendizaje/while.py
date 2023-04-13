###CURSO DE FUNDAMENTOS DE PYTHON

#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
############ MENU DE OPCIONES ##########################
    
#1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada número en la pantalla.
def contador_asc(num):
    cont=0
    while cont<= num:
        print(cont)
        cont+=1
#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.
def contador_des(num):
    while num>=0:
        print(num)
        num-=1
#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese número y lo imprima en la pantalla.
def suma_numeros(num):
    cont=0
    suma=0
    while cont<= num:
        cont+=1
        suma+= cont
    return suma - (num +1)
num=int(input("INGRESE UN NUMERO: "))
print (suma_numeros (num))
    
#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla. El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.
def factorial(num):
     cont=1
     mul=1
     while cont <= num:
        mul=mul*cont
        cont+=1
     return mul
num=int(input("INGRESE UN NUMERO: "))
print (factorial (num))

#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al número generado, el programa debe imprimir "El número que buscas es menor". Si el usuario ingresa un número menor al número generado, el programa debe imprimir "El número que buscas es mayor". Si el usuario adivina el número, el programa debe imprimir "¡Felicitaciones, adivinaste el número!" y terminar.
def adivinar_numero(aleatorio):
    adivinanza=0
    while adivinanza != aleatorio:
        adivinanza=int(input("adivine el numero entre 1 y 10"))
        if adivinanza > aleatorio:
            print ("el numero es mayor al numero a adivinar")
        elif adivinanza < aleatorio:
            print("el numero es menor al numero a adivinar")
        else:
            print("adivinaste",adivinanza)
  
#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de vocales que tiene esa cadena. Para simplificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.
def vocales (cadena):
    contador_vocales=0
    i=0
    while i < len(cadena):
        if cadena[i].lower() in "aeiou":
            contador_vocales+=1
        i+=1
    return contador_vocales

#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números pares desde cero hasta ese número y lo imprima en la pantalla.
def suma_pares(numero):
    sumatoria=0
    contador=0
    while contador <= numero:
        if contador%2==0:
          sumatoria+=contador
        contador+1
    return sumatoria
 

#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros positivos: una base y un exponente. Utilizando un bucle while, calcule la potencia de la base elevada al exponente y lo imprima en la pantalla.
def potencia (base,exp):
    resultado=1
    contador=1
    while contador<= exp:
         resultado*=base
         contador+=1
    return resultado

#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números y, utilizando un bucle while, calcule el promedio de esos números y lo imprima en la pantalla.
def promedio (valores):
     sumatoria=0
     contador=0
     while contador<len(valores):
         sumatoria=sumatoria+int(valores[contador])
         contador+=1
     print(sumatoria/len(valores))

#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena. Para simplificar el problema, puedes considerar que las palabras están separadas por espacios en blanco.
def palabras(cadena):
     contador=0
     indice=0
     if len(cadena)==0:
         contador=0
     else:
         contador+1
     while indice<len(cadena):
         if cadena[indice]==' ':
             contador+1
         indice +=1
     return contador
opcion=1
while opcion>=0 and opcion<=10:
    print("############## MENU DE OPCIONES ####################")
    print("1. CONTADOR ASCENDENTE ")
    print("2. CONTADOR DESCENDENTE")
    print("3. SUMA DE NUMEROS")
    print("4. FACTORIAL")
    print("5. ADIVINAR EL NUMERO")
    print("6. CONTADOR DE VOCALES")
    print("7. SUMA DE NUMEROS PARES")
    print("8. CALCULO DE POTENCIA")
    print("9. CALCULO DE PROMEDIO")
    print("10. CONTADOR DE PALABRAS")
    print("0. SALIR")
    opcion=int(input("DIGITE UNA OPCION: "))
    if opcion==0:
        print("HA SELECIIONADO LA OPCION SALIR")
        break
    elif opcion==1:
        print("CONTADOR ASCENDENTE")
        num=int(input("INGRESE UN NUMERO ENTERO POSITIVO: "))
        contador_asc(num)
    elif opcion==2:
        print("CONTADOR DESCENDENTE")
        num=int(input("INGRESE UN NUMERO ENTERO POSITIVO: "))
        contador_des(num)
    elif opcion==3:
        print("SUMA DE NUMEROS")
        num=int(input("INGRESE UN NUMERO ENTERO POSITIVO: "))
        suma_numeros(num)
    elif opcion==4:
        print("FACTORIAL")
        num=int(input("INGRESE UN NUMERO ENTERO POSITIVO: "))
        print(factorial(num))
    elif opcion==5:
        print("ADIVINAR UN NUMERO")
        import random
        aleatorio=random.randint(1,100)
        adivinar_numero (aleatorio)
    elif opcion==6:
        print("CONTADOR DE VOCALES")
        texto= input("INGRESE UNA CADENA DE TEXTO EN MINUSCULA: ")
        print ("SU TEXTO TIENE",vocales(texto),"VOCALES")
    elif opcion==7:
        print("SUMA DE NUMEROS PARES")
        numero= input("INGRESE UN NUMERI: ")
        print("DE EL NUMERO",numero,"que ingreso solo se sumo los pares =",suma_pares(numero))
    elif opcion==8:
        print("CALCULO DE POTENCIA")
        base=int(input("INGRESE LA BASE: "))
        exp=int(input("INGRESE  EL EXPONENTE: "))
        print ("Su base",base,"elevado al exponente",exp,"=",potencia(base,exp))
    elif opcion==9:
        print("CALCULO DE PROMEDIO")
        valores= input("INGRESE NUMEROS SEPARADOS POR COMAS: ").split(',')
        promedio(valores)
    elif opcion==10:
        print("CONTADOR DE PALABRAS")
        cadena= input("INGRESE UNA CADENA DE TEXTO SEPARADO POR ESPACIOS: ")
        print ("la cadena de texto tiene",palabras(cadena),"palabras")
else:
    print("HA INGRESADO UN VALOR DIFERENTE AL MENU")