#Ejercicio 1
#Crear lista de notas

notas = [7, 4, 9, 8, 3, 7, 5, 8, 9, 4]
sumatoria = 0
cont = 0
print("Notas: ")
for n in notas:
    print(n, end=" ")
print()

promedio = sum(notas) / len(notas)

print("el promedio de notas es : ", promedio)

print("La nota mas alta es: ", max(notas))
print("La nota mas baja es: ", min(notas))

#Ejercicio 2

productos = []

for i in range(5):
    producto = input(f"Ingrese el producto {i + 1}: ")
    productos.append(producto)
productos_ordenados = sorted(productos)
print("lista de productos ordenados alfabeticamente")

print(productos_ordenados)

eliminar = input("Escriba el producto que desea eliminar de la lista: ")
productos_ordenados.remove(eliminar)
print("Lista actualizada: ")
print(productos_ordenados)

#Ejercicio 3

import random

numeros = []
numeros_pares = []
numeros_impares = []
for num in range(15):
    num = random.randint(1,100)
    numeros.append(num)
    if num % 2 == 0:
         numeros_pares.append(num)
    else:
         numeros_impares.append(num)


print(numeros)
print(numeros_pares)
print("La cantidad de numeros pares es de: ", len(numeros_pares))
print(numeros_impares)
print("La cantidad de numeros impares es de: ", len(numeros_impares))

#Ejercicio 4

datos = [1, 3, 5, 7, 1, 9, 5, 3]

datos_sin_repetir = set(datos)
print(datos_sin_repetir)

#Ejercicio 5

estudiantes = ["Juan", "Pedro", "Maria", "Andrea", "Javier", "Lorena", "Francisco", "Fernando"]


accion = input("Escriba 1 si desea agregar un estudiante o 2 si desea eliminarlo: ")

if accion == "1":
    ingreso = input("Escriba el nombre del alumno: ")
    estudiantes.append(ingreso)
    print("La lista actualizada es: ")
    print(estudiantes)
elif accion == "2":
    eliminado = input("Escriba el nombre del alumno a eliminar: ").capitalize()
    if eliminado in estudiantes:
        estudiantes.remove(eliminado)
        print("La lista actualizada es: ")
        print(estudiantes)
    else: 
        print("No se ha encontrado el estudiante solicitado")

#Ejercicio 6

numeros = [1, 2, 3, 4, 5, 6, 7]

lista_nueva = [numeros[-1]] + numeros[:-1]

print(lista_nueva)

#Ejercicio 7

temperaturas = [
    [12, 20],
    [14, 22],
    [11, 19],
    [13, 23],
    [15, 25],
    [10, 18],
    [16, 26]
]


minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]

promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)


print("El promedio de temperaturas minimas de la semana es de ", promedio_min)
print("El promedio de temperaturas maximas de la semana es de ", promedio_max)

amplitudes = [dia[1] - dia[0] for dia in temperaturas]
mayor_amplitud = max(amplitudes)
dia_mayor_amplitud = amplitudes.index(mayor_amplitud) + 1 

print("La mayor amplitud termica fue de", mayor_amplitud, "grados el dia: ", dia_mayor_amplitud)

#Ejercicio 8

#Matriz de 3 notas cada 5 estudiantes.

notas = [
    [7, 8, 9],  # Estudiante 1
    [6, 7, 8],  # Estudiante 2
    [5, 6, 7],  # Estudiante 3
    [9, 8, 10], # Estudiante 4
    [4, 5, 6]   # Estudiante 5
]
#promedio de cada estudiante

print("Promedio de cada estudiante")

for i in range(len(notas)):
    promedio_estud = sum(notas[i]) / (len(notas[i]))
    print("Estudiante", i + 1, ":", round(promedio_estud, 2))

#promedio por materia

print("Promedio por materia")

materia = len(notas[0])
for j in range(materia):
    promedio_mat = sum(notas[i][j] for i in range(len(notas))) / len(notas)
    print("Materia", j + 1, ":", promedio_mat)

#Ejercicio 9

#Creacion del tablero de Ta-Te-Ti vacio

tablero = []

#armo cada fila con "-" y la agrego a tablero

for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

#Muestro tablero

for fila in tablero:
    for celda in fila:
        print(celda, end= " ")
    print()

#juego

jugador = "X"
jugada = 0

while jugada < 9 :
    print("\nTurno del jugador", jugador)

    fila = int(input("ingrese la fila (0-2): "))
    columna = int(input("ingrese la columna (0-2): "))
#verificar la correcta entrada de fila y columna
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posicion fuera de rango. Intente de nuevo")
        continue #vuelve a pedir la jugada
#verificar que la casilla no este ocupada
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugada += 1
    else:
        print("Casilla ocupada. Intente nuevamente")
        continue #pide la jugada nuevamente

    for fila in tablero:
        for celda in fila:
            print(celda, end= " ")
        print()

    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

#Ejercicio 10

ventas = [
    [10, 12, 8, 15, 9, 11, 7],   # Producto 1
    [5, 7, 6, 8, 10, 12, 9],     # Producto 2
    [20, 18, 25, 22, 19, 17, 21],# Producto 3
    [3, 4, 2, 5, 6, 4, 3]        # Producto 4
]

#Total vendido por cada producto

print("Total vendido por cada producto")
totales_productos = []

for i in range(4):
    total = sum(ventas[i])
    totales_productos.append(total)
    print("Producto", i + 1, ":", total )
    

#Dia con mayor venta

totales_dias =[]

for j in range(7):
    total = 0
    for i in range(4):
        total += ventas[i][j]
    totales_dias.append(total)
    

dia_max = totales_dias.index(max(totales_dias)) + 1
print("El día con mayores ventas totales fue el Día", dia_max, "con", max(totales_dias),"unidades")

#Producto mas vendido en la semana

prod_max = totales_productos.index(max(totales_productos)) + 1
print("El producto mas vendido en la semana fue el producto", prod_max, "con", max(totales_productos),"unidades")