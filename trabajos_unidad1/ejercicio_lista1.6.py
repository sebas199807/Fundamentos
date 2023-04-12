#EJERCICIOS DE DICCIONARIOS
"""
Nombre: Ariel Villa
Carrera: Big Data
"""

"""1.Crea un diccionario vacío y agrega tres elementos de la siguiente forma: "clave": valor"""

dic = {}
dic['Clave 1'] = 1
dic['Clave 2'] = 11
dic['Clave 3'] = 111
dic['Clave 4'] = 1111
dic['Clave 5'] = 11111

"""2.Dado el siguiente diccionario:"""

personas = {"Juan": 28, "María": 20, "Pedro": 32, "Ana": 25}

#a) Imprime la edad de Juan.
print(personas["Juan"])

#b) Agrega un nuevo elemento al diccionario con la clave "Luis" y la edad 18.
personas["Luis"] = 18

#c) Elimina el elemento con la clave "Pedro".
personas.pop("Pedro")

"""3.Dado el siguiente diccionario:"""

ventas = {"manzanas": 10, "naranjas": 5, "peras": 8}

#a) Imprime la cantidad de manzanas vendidas.
print(ventas["manzanas"])

#b) Agrega 3 elementos más al diccionario: "limones": 12, "sandías": 3, "melones": 5.
ventas["limones"] = 12
ventas["sandias"] = 3
ventas["melones"] = 5
 
#c) Imprime las claves del diccionario.
print(ventas.keys())

"""4. Dado el siguiente diccionario:"""

alumnos = {"Juan": {"edad": 22, "promedio": 8.5}, "María": {"edad": 20, "promedio": 9.0}, "Pedro": {"edad": 25, "promedio": 7.5}}

#a) Imprime la edad de Juan.
print(alumnos["Juan"]["edad"])

#b) Imprime el promedio de María.
print(alumnos["María"]["promedio"])

#c) Agrega un nuevo elemento al diccionario con la clave "Ana" y los valores "edad": 19 y "promedio": 8.0.0
alumnos["Ana"] = {"edad": 19, "promedio": 8.0}


"""5. Dado el siguiente diccionario:"""

empleados = {"Juan": {"departamento": "Ventas", "sueldo": 1500}, "María": {"departamento": "Contabilidad", "sueldo": 1800}, "Pedro": {"departamento": "Ventas", "sueldo": 1700}, "Ana": {"departamento": "Recursos Humanos", "sueldo": 1900}}

#a) Imprime el sueldo de Pedro.
print(empleados["Pedro"]["sueldo"])

#b) Cambia el sueldo de Ana a 2000.
empleados["Ana"]["sueldo"]= 2000
print(empleados)

#c) Crea un nuevo diccionario con los empleados del departamento de Ventas.
lista=[]
disct=dict()
for c,v in empleados.items():
    for a,b in v.items():
        if b=="Ventas":
            lista.append(c)
            disct[c]={a:b}
print(lista)
print(disct)

"""6.Dado el siguiente diccionario:"""
cursos = {
    "Pedro": ["Matemáticas", "Biología", "Historia"],
    "María": ["Física", "Química", "Literatura"]
}

#a) Imprime las materias en las que está inscrito Pedro.
print(cursos["Pedro"])

#b) Agrega una materia más a la lista de materias de María: "Programación".
cursos["María"].append("Programación")
print(cursos)

#c) Crea un nuevo diccionario con los estudiantes que están inscritos en la materia de Biología.
estudiantes_biologia = {}

for estudiante, cursos in cursos.items():
    if "Biología" in cursos:
        estudiantes_biologia[estudiante] = cursos
        
print(estudiantes_biologia)

"""7. Dado el siguiente diccionario:"""

productos = {'manzanas': 2.99, 
             'naranjas': 1.99, 
             'peras': 3.99, 'uvas': 4.99, 
             'kiwis': 0.99, 'duraznos': 2.49}
stock = {'manzanas': 100, 'naranjas': 50, 'peras': 25, 'uvas': 75, 'kiwis': 200, 'duraznos': 60}

#a) Imprime el precio de las naranjas.
print(productos["naranjas"])

#b) Cambia el stock de peras a 12.
stock["peras"] = 12
print(stock)

#c) Crea una función que calcule el valor total de los productos en el diccionario.
def calcular_valor_total(productos, stock):
    total = 0
    for producto, precio in productos.items():
        if producto in stock:
            total += precio * stock[producto]
    return total