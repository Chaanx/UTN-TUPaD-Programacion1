
#Inicio actividad 1

cont = 0

while 0 <= cont < 100:

    print(cont)
    cont+=1

#Inicio actividad 2

numero = (input("Ingrese un numero entero: "))
cant_digitos = len(numero)
print("El numero ingresado tiene", cant_digitos, "digitos")

#Inicio actividad 3

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))


if numero1 > numero2:
    numero1, numero2 = numero2, numero1

suma = 0
for i in range(numero1+1, numero2):
    suma += i
print("La suma de los numeros entre", numero1, "y", numero2, "es: ", suma)

#Inicio actividad 4


num = int(input("ingrese un numero: "))
suma = 0

while  num != 0:
    suma += num
    print(suma)
    num = int(input("ingrese un numero: "))
    
print("El total acumulado es", suma)


#Inicio actividad 5

import random

numero = random.randint(0,9)
intentos = 0
adivinar_numero = int(input("Adivina el numero (entre 0 y 9): "))
while adivinar_numero != numero:
    intentos += 1
    print("Incorrecto! Intenta nuevamente: ")
    adivinar_numero =int(input("Adivina el numero (entre 0 y 9): "))
   
intentos +=1
print("Correcto! Adivinaste en", intentos, "intento(s)")

#Inicio actividad 6

for x in range(100,-1,-2):
  
     print(x)

#Inicio actividad 7

suma = 0
numero = int(input("Ingrese un numero: "))

for i in range(0, numero + 1):
    suma += i

print("La suma de los numeros de 0 a", numero, "es", suma)

#Inicio actividad 8

cont_pares = 0
cont_impares = 0
cont_positivos = 0
cont_negativos = 0 


for i in range(0,100):
   
    i = int(input("ingrese un numero: "))
    
    if i % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1

    if i > 0:
        cont_positivos += 1
    elif i < 0:
        cont_negativos += 1 

print("Resultados:")
print("La cantidad de numeros pares es:", cont_pares)
print("La cantidad de numeros impares es:", cont_impares)
print("La cantidad de numeros positivos es:", cont_positivos)
print("La cantidad de numeros negativos es:", cont_negativos)

#Inicio actividad 9

cont = 0
suma = 0
for i in range(100):

    i = int(input("Ingrese un numero: "))
    cont +=1
    suma += i
print("La media de estos valores es:", suma / cont)

#Inicio actividad 10

numero = int(input("Ingresa un número: "))
numero_invertido = 0


es_negativo = False
if numero < 0:
    es_negativo = True

    numero = abs(numero)


while numero != 0:
   
    digito = numero % 10
   
    numero_invertido = numero_invertido * 10 + digito

    numero = numero // 10


if es_negativo:
    numero_invertido = -numero_invertido

print("Número invertido:", numero_invertido)



