
#Ejercicio 1
print("Hola mundo")
#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola,", nombre,"!")
#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia:")
print(f"Hola, soy ", nombre, apellido,", tengo", edad, "años y resido en ", residencia)

#Ejercicio 4
radio = int(input("Ingrese el radio: "))
pi = 3.14159
print("El area del circulo es: ", pi * radio**2)
print("El perimetro del circulo es: ", 2 * pi * radio)
#Ejercicio 5
segundos = int(input("Ingrese una cantidad de segundos: "))
print(F"Los segundos ingresados equivalen aun total de ", segundos / 3600, "horas")
      
#Ejercicio 6
numero = int(input("Introduce un número para mostrar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del ", numero )

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
#Ejercicio 7
numero_1 = int(input("ingrese un numero positivo: "))
numero_2 = int(input("ingrese otro numero positivo: "))

print(f"La suma de ", numero_1, "y", numero_2, "da como resultado: ", numero_1 + numero_2)
print(f"La resta de ", numero_1, "y", numero_2, "da como resultado: ", numero_1 - numero_2)
print(f"La multiplicacion entre ", numero_1, "y", numero_2, "da como resultado: ", numero_1 * numero_2)
print(f"La division entre ", numero_1, "y", numero_2, "da como resultado: ", numero_1 / numero_2)
#Ejercicio 8
peso = int(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

print(f"Su indice de masa corporal es de: ", peso / (altura **2))
#Ejercicio 9
temperatura = int(input("Ingrese la temperatura en grados celsius: "))

print(f"La temperatura en grados fahrenheit es de: ", 9/5 * temperatura + 32)
#Ejercicio 10
numero_1 = int(input("Ingrese el primer valor: "))
numero_2 = int(input("Ingrese el segundo valor: "))
numero_3 = int(input("Ingrese el tercer valor: "))
 
print(f"El promedio entre los tres valores es de : ", (numero_1 + numero_2 + numero_3) / 3 ) 