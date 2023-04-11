def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicacion(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def saludo():
    print("Hola Sebas")
def formateo (nombre,apellido):
    print(nombre,apellido)
bandera=True
while bandera:
    print("MENU DE OPCIONES")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")
    print("5. SALUDO")
    print("6. FORMATEO")
    print("7. SALIR")
    opcion=int(input("INGRESE UNA OPCION "))
    if opcion!=7:
        num1=int(input("INGRESE NUMERO 1: "))
        num2=int(input("INGRESE NUMERO 2: "))
        if opcion==1:
            print("la suma es igual a:", suma(num1,num2))
        elif opcion==2:
            print("la resta es igual a:", resta(num1,num2))
        elif opcion==3:
            print("la multiplicacion es igual a:",multiplicacion(num1,num2))
        elif opcion==4:
            print("la division es igual a:", division(num1,num2))
        elif opcion==5:
            saludo()
        elif opcion==6:
            formateo ()
        elif opcion==7:
            print()
    else:
        bandera=False
        print("fin de ciclo")
print("nueva linea")