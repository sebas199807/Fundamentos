#EJERCICIOS DE CONJUNTOS
"""
Nombre: Ariel Villa
Carrera: Big Data
"""

#Crear un conjunto con los números del 1 al 10 e imprimirlo en pantalla.

numeros = set(range(1, 11))
print(numeros)


#Crear dos conjuntos, uno con los números pares del 1 al 10 y otro con los impares del 1 al 10. Luego, imprimir los conjuntos y la intersección entre ellos.

# Crear conjunto de números pares
pares = set(range(2, 11, 2))

# Crear conjunto de números impares
impares = set(range(1, 11, 2))

# Imprimir conjuntos
print("Conjunto de pares:", pares)
print("Conjunto de impares:", impares)

# Encontrar intersección
interseccion = pares & impares

# Imprimir intersección
print("Intersección:", interseccion)


#Crear un conjunto con los elementos "manzana", "banana" y "naranja". Luego, pedirle al usuario que ingrese un elemento y determinar si ese elemento se encuentra en el conjunto o no.

# Crear conjunto
frutas = {"manzana", "banana", "naranja"}

# Pedir entrada al usuario
entrada = input("Ingrese una fruta: ")

# Verificar si la entrada está en el conjunto
if entrada in frutas:
    print("La fruta", entrada, "se encuentra en el conjunto.")
else:
    print("La fruta", entrada, "no se encuentra en el conjunto.")


#Crear un conjunto con los números del 1 al 5 y otro con los números del 4 al 8. Luego, unir los conjuntos y eliminar los elementos repetidos. Finalmente, imprimir el conjunto resultante.

# Crear conjuntos
conjunto1 = set(range(1, 6))
conjunto2 = set(range(4, 9))

# Unir los conjuntos
conjunto_unido = conjunto1.union(conjunto2)

# Eliminar los elementos repetidos
conjunto_sin_repetidos = set()
for elemento in conjunto_unido:
    if elemento not in conjunto_sin_repetidos:
        conjunto_sin_repetidos.add(elemento)

# Imprimir el conjunto resultante
print(conjunto_sin_repetidos)


#Crear un conjunto con los elementos "leche", "pan", "huevos" y "azúcar". Luego, eliminar el elemento "azúcar" del conjunto y agregar el elemento "harina". Finalmente, imprimir el conjunto resultante.

# Crear conjunto
compras = {"leche", "pan", "huevos", "azúcar"}

# Eliminar elemento "azúcar" del conjunto
compras.remove("azúcar")

# Agregar elemento "harina" al conjunto
compras.add("harina")

# Imprimir conjunto resultante
print(compras)


#Crear un conjunto con los nombres "Juan", "María", "Pedro" y "Luisa". Luego, imprimir el número de elementos del conjunto.

# Crear conjunto
nombres = {"Juan", "María", "Pedro", "Luisa"}

# Imprimir número de elementos del conjunto
print(len(nombres))


#Crear dos conjuntos, uno con los números del 1 al 5 y otro con los números del 4 al 8. Luego, imprimir los conjuntos y la diferencia simétrica entre ellos.

# Crear conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Imprimir conjuntos
print("conjunto1:", conjunto1)
print("conjunto2:", conjunto2)

# Imprimir diferencia simétrica
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print("diferencia simétrica:", diferencia_simetrica)


#Crear un conjunto con los números del 1 al 10 y otro con los números del 5 al 15. Luego, imprimir los conjuntos y la unión entre ellos.

# Crear conjuntos
conjunto1 = set(range(1, 11))
conjunto2 = set(range(5, 16))

# Imprimir conjuntos
print("conjunto1:", conjunto1)
print("conjunto2:", conjunto2)

# Imprimir unión
union = conjunto1.union(conjunto2)
print("unión:", union)


#Crear un conjunto con los elementos "manzana", "banana", "naranja" y "pera". Luego, imprimir los elementos del conjunto en orden alfabético.

# Crear conjunto
frutas = {"manzana", "banana", "naranja", "pera"}

# Imprimir elementos en orden alfabético
print(sorted(frutas))


#Crear un conjunto con los números del 1 al 10 y otro con los números del 6 al 15. Luego, imprimir los conjuntos y la intersección entre ellos.

# Crear conjuntos
conjunto1 = set(range(1, 11))
conjunto2 = set(range(6, 16))

# Imprimir conjuntos
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Calcular intersección
interseccion = conjunto1.intersection(conjunto2)

# Imprimir intersección
print("Intersección:", interseccion)