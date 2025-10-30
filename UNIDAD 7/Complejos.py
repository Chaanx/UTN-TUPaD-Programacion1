#Ejercicio 1

precios_frutas = {'Banana' : 1200, 'Anana' : 2500, 'Melon' : 3000, 'Uva' : 1450}

#Agregar elementos al diccionario

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


#Ejercicio 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Pera'] = 2800

print(precios_frutas)

#Ejercicio 3

frutas = precios_frutas.keys()

print(frutas)

#Ejercicio 4

agenda = {}
datos = 0

while datos < 5:

    nombres = input("Ingrese el nombre de la persona que desea agendar: ")
    numero = input("Ingrese el numero telefonico: ")
    datos +=1
    agenda[nombres] = numero

print(agenda)
    
contacto = input("Ingrese un nombre para saber si esta agendado: ")

 
if contacto in agenda:
    numero = agenda[contacto]
    print(f"{contacto} tiene el numero {numero}")
else:
    print("El contacto no se encuentra agendado")


#Ejercicio 5

frase = input("Ingrese una frase: ")

palabras = set()
cant_palabras = {}

for palabra in frase.split():
    palabras.add(palabra)
print(palabras)

for palabra in frase.lower().split():
    if palabra in cant_palabras:
        cant_palabras[palabra] += 1
    else:
        cant_palabras[palabra] = 1

#for palabra, cantidad in cant_palabras.items():
print(f"{cant_palabras}")


#Ejercicio 6

alumnos = {}

dato = 0

while dato < 3:

    nombre = input("Ingrese el nombre del alumno: ")
   
    nota = input("Ingrese 3 notas separadas por espacio:")
    notas = tuple(map(float, nota.split()))
    dato +=1
    alumnos[nombre] = notas

print("Promedio de los alumnos")

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"-{nombre}: {round(promedio, 2)}")

#Ejercicio 7

parcial1 = {'Juan', 'Pedro', 'Maria', 'Clara', "Jorge"}

parcial2 = {'Juan', 'Pedro', 'Diego', 'Clara', "Sofia"}

#Estudiantes que aprobaron ambos parciales (interseccion)
ambos = parcial1 & parcial2
print("Estudiantes aprobados en ambos parciales:", ambos)

#Estudiantes que aprobaron solo 1 de los parciales (diferencia simetrica)
un_solo_parcial = parcial1 ^ parcial2

print("Solo aprobaron un parcial :", un_solo_parcial)

#Estudiantes que aprobaron al menos un parcial (union)
al_menos_uno = parcial1 | parcial2

print("Estudiantes que aprobaron al menos un parcial:", al_menos_uno)


#Ejercicio 8

productos = {'remera': 10 , 'pantalon': 18, 'saco': 14, 'vestido': 6}

producto = input("Consulte el stock de: ")
if producto in productos:
    print(f"Hay {productos[producto]} unidades disponibles")
else:
    print("El producto no ha sido encontrado")

modificar_stock = input("Ingrese el producto a modificar: ")
cantidad = int(input("Ingrese el nuevo stock: "))
if modificar_stock in productos:
    productos[modificar_stock] = cantidad
    print(f"{modificar_stock} tiene {cantidad} unidades")
else:
    print("Producto no encontrado")
print(productos)

nuevo_producto = input("Ingrese el nuevo producto: ")


if not nuevo_producto in productos:
    stock_nuevo_prod = int(input("Ingrese el stock: "))
    productos[nuevo_producto] = stock_nuevo_prod
    print(productos)
else:
    print("El producto ya existe")


#Ejercicio 9

agenda = {
    ("Lunes", "09:00"): "Reunión de equipo",
    ("Martes", "14:30"): "Clase de inglés",
    ("Miércoles", "18:00"): "Entrenamiento de fútbol",
    ("Jueves", "11:00"): "Consulta médica",
    ("Viernes", "20:00"): "Cena con amigos"
}

dia = input("Ingrese el dia a verificar: ").capitalize()
hora = input("Ingrese la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay actividades programadas en ese horario")



#Ejercicio 10

# Diccionario original: país: capital
paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio",
    "Brasil": "Brasilia",
    "Italia": "Roma"
}

# Diccionario invertido: capital: país
capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais

# Mostrar el nuevo diccionario
print("Diccionario invertido (capital: país):")
for capital, pais in capitales.items():
    print(f"- {capital}: {pais}")