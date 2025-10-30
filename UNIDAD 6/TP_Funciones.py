#Ejercicio 1

#definir funcion
def imprimir_hola_mundo():
    return "Hola Mundo!"

#imprimir saludo
print(imprimir_hola_mundo())


#ejercicio 2

#definir funcion
def saludar_usuario(nombre):
    return f"Hola {nombre}!"


#crear programa

nombre = input("Ingrese su nombre: ")

print(saludar_usuario(nombre))


#Ejercicio 3

#definir funcion
def informacion_personal(nombre,apellido,edad,residencia):
    return nombre, apellido, edad, residencia

#crear programa

nombre = input("Ingrese su nombre: ").capitalize()
apellido = input("Ingrese su apellido: ").capitalize()
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ").capitalize()

datos = informacion_personal(nombre, apellido, edad, residencia)

print(f"Soy {datos[0]} {datos[1]}, tengo {datos[2]} años y vivo en {datos[3]}")



#ejercicio 4
import math

#definir funciones
def calcular_area_circulo(radio):
    area = round(math.pi * radio ** 2, 3)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = round(2 * math.pi* radio, 3)
    return perimetro

#crear programa

radio = float(input("Por favor, ingrese el radio: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es {area} y el perímetro es {perimetro}")


#Ejercicio 5

#definir funcion
def segundos_a_horas(segundos):
    return segundos / 3600

#crear programa
segundos = int(input("Ingrese los segundos que desea convertir en horas: "))


print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")


#Ejercicio 6

#definir funcion

def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


#crear programa

numero = int(input("Ingrese el numero cuya tabla desee imprimir: "))

tabla_multiplicar(numero)


#Ejercicio 7

#definir funcion

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

#crear programa

x = float(input("Ingrese un número: "))
y = float(input("Ingrese otro número: "))

suma, resta, multiplicacion, division = operaciones_basicas(x,y)

print(f"La suma de ambos números es {suma}")
print(f"La resta de ambos números es {resta}")
print(f"La multiplicación entre ambos números es {multiplicacion}")
print(f"La división entre ambos números es {division}")


#ejercicio 8

#definir función

def calcular_imc(peso,altura):
    return round(peso / altura, 2)

#crear programa

peso = float(input("Ingrese su peso (en Kg): "))
altura = float(input("Ingrese su altura (en metros): "))

print(f"Su índice de masa corporal es {calcular_imc(peso,altura)}")


#Ejercicio 9

#definir función

def celsius_a_fahrenheit(celsius):
    return temperatura_C * (9 / 5) + 32

#crear programa

temperatura_C = float(input("Ingrese la temperatura que desea convertir (°C): "))


print(f"{temperatura_C} °C equivale a {celsius_a_fahrenheit(temperatura_C)} °F")


#Ejercicio 10

#definir función

def calcular_promedio(a,b,c):
    return round((a + b + c) / 3, 2)
#crear programa

x = float(input("Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))
z = float(input("Ingrese el tercer número: "))

print(f"El promedio de los números ingresados es {calcular_promedio(x,y,z)}")