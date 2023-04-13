from funciones import*
opcion=0
while opcion >=0 and opcion<=10:
    print ("MENU DE OPCIONES")
    print ("1.SUMA")
    print ("2.RESTA")
    print ("3.MULTIPLICACION")
    print ("4.DIVISION")
    print ("0. SALIR")
    opcion=int(input("INGRESE UNA OPCION: "))
    if opcion==0:
        print("HA SELECCIONADO SALIR")
        break
    elif opcion==1:
        a=int(input("INGRESE EL PRIMER NUMERO: "))
        b=int(input("INGRESE EL SEGUNDO NUMERO: "))
        print("EL RESULTADO DE LA SUMA ES: ", suma(a,b))
    elif opcion==2:
        a=int(input("INGRESE EL PRIMER NUMERO: "))
        b=int(input("INGRESE EL SEGUNDO NUMERO: "))
        print("EL RESULTADO DE LA RESTA ES: ", resta(a,b))
    elif opcion==3:
        a=int(input("INGRESE EL PRIMER NUMERO: "))
        b=int(input("INGRESE EL SEGUNDO NUMERO: "))
        print("EL RESULTADO DE LA MULTIPLICACION ES: ", multi(a,b))
    elif opcion==4:
        a=int(input("INGRESE EL PRIMER NUMERO: "))
        b=int(input("INGRESE EL SEGUNDO NUMERO: "))
        print("EL RESULTADO DE LA DIVISION ES: ", division(a,b))
    else:
        print("OPCION INGRESADA INCORRECTA")




