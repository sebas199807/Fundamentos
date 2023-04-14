########################### MENU DE OPCIONES #####################################
from metodos import*

opcion =  1
while opcion >= 0 and opcion <=10 :

    print("############### MENU DE OPCIONES ######################")
    print(" 1.- Contador Ascendente")
    print(" 2.- Contador Descendente")
    print(" 3.- Suma de Numeros")
    print(" 4.- Factorial")
    print(" 5.- Adivinar el numero")
    print(" 6.- Contador de Vocales")
    print(" 7.- Suma de numeros pares")
    print(" 8.- Calculo de potencia")
    print(" 9.- Calculo de Promedio")
    print(" 10.- Contador de Palabras")
    print(" 0.- Salir")

    opcion = int(input("Digite la opcion, deseada: "))

    if opcion == 0:

        print("Ha seleccionado la opccion Salir \n\tQue tenga Buen Dia")
        break

    elif opcion == 1:

        print("Ha selecionado la opcion 1 : \n\tContador Ascendente")
        num = int(input("Ingrese el numero deseado: "))
        contador_ascendente(num)

    elif opcion == 2:

        print("Ha selecionado la opcion 2 : \n\tContador Descendente")
        num = int(input("Ingrese un numero: "))
        contador_descendente(num)

    elif opcion == 3:

        print("Ha selecionado la opcion 3 : \n\tSuma de Numeros")
        num = int(input("Ingrese un numero: "))
        print(suma_numeros(num))

    elif opcion == 4:

        print("Ha selecionado la opcion 4 : \n\tFactorial")
        num = int(input("Ingrese un numero: "))
        print(factorial(num))   

    elif opcion == 5:

        print("Ha selecionado la opcion 5 : \n\tAdivinar el numero")
        num = random.randint (1 ,10)
        adivinar_num(num)

    elif opcion == 6:

        print("Ha selecionado la opcion 6 : \n\tContador de Vocales")
        cadena = input("Ingrese la palabra:")
        contar_vocales(cadena)

    elif opcion == 7:

        print("Ha selecionado la opcion 7 : \n\tSuma de numeros pares")
        num = int(input("Ingresa un número entero positivo: "))
        numeros_pares(num)

    elif opcion == 8:

        print("Ha selecionado la opcion 8 : \n\tCalculo de potencia")
        numero = 0
        numero = int(input("Ingrese un numero:"))
        exponente = int(input("Ingrese el exponente: "))
        print(potencia(numero, exponente))

    elif opcion == 9:

        print("Ha selecionado la opcion 9 : \n\tCalculo de Promedio")
        numeros = input("Ingresa una lista de números separados por comas: ")
        numeros = numeros.split(",")
        calculo_promedio(numeros)


    elif opcion == 10:

        print("Ha selecionado la opcion 10 : \n\tContador de Palabras")
        cadena = input("Ingrese la frase: ")
        contador_palabras(cadena)