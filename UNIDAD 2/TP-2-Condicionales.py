#Ejercicio 1

edad_usuario = int(input("Ingrese su edad: "))

if edad_usuario >= 18:
    print("Es mayor de edad")

#Ejercicio 2

print("Ejercicio numero 2")


nota_usuario = int(input("Ingrese su nota: "))

if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3

print("Ejercicio numero 3")

numero_par = int(input("Ingrese un numero par: "))

if numero_par % 2  == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#Ejercicio 4

print("Ejercicio numero 4")

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif  12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio 5

print("Ejercicio numero 5")

contrasenia = input("Ingrese una contraseña entre 8 y 14 caracteres ")

if 8 <= len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta")

else:
    Print("Por favor, ingrese una contraseña entre 8 y 14 caracteres")



#Ejercicio 6

print("Ejercicio numero 6")


import random
from statistics import multimode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

mi_lista = numeros_aleatorios

media = mean(mi_lista)
mediana = median(mi_lista)
modas = multimode(mi_lista)
moda = modas[0]

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar sesgo claro")

print(f"La lista obtenida es: ", mi_lista, "Media: ", media, ", Mediana: ", mediana, ", Moda: ", moda)


#Ejercicio 7

print("Ejercicio numero 7")


frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower() in "aeiou":
    frase += "!"
    print(frase)


#Ejercicio 8

print("Ejercicio numero 8")

nombre = input("Ingrese su Nombre: ")
opcion = int(input("Ingrese 1, 2 o 3 si quiere su nombre en mayúsculas, en minúsculas o con la primera letra mayúscula: "))
               
if opcion == 1:
    print(nombre.upper())   
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opcion no valida")

#Ejercicio 9

print("Ejercicio numero 9")


magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitud_terremoto < 3:
    print("Muy leve.(Imperceptible)")
elif 3 <= magnitud_terremoto < 4:
    print("Leve. (Ligeramente perceptible)")
elif 4 <= magnitud_terremoto < 5:
    print("Moderado. (Sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud_terremoto < 6:
    print("Fuerte. (puede causar daños en estructuras debiles)")
elif 6 <= magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print( "Extremo. (puede causar graves daños a gran escala)")
else:
    print("Dato invalido")



#Ejercicio 10

print("Ejercicio numero 10")


def determinar_estacion(dia, mes):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        return "invierno" 
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        return "primavera"  # Ajuste para hemisferio norte, sería "Primavera" en hemisferio sur
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        return "Verano"  # Ajuste para hemisferio norte, sería "Invierno" en hemisferio sur
    else:
        return "otoño"  # Ajuste para hemisferio norte, sería "Otoño" en hemisferio sur

def determinar_estacion_hemisferio_sur(dia, mes):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        return "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        return "Invierno"
    else:
        return "Primavera"

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
hemisferio = input("Ingrese el hemisferio (Norte/Sur): ")
    
if hemisferio.lower() == "norte":
        estacion = determinar_estacion(dia, mes)
        print(f"La estación es: {estacion}")
elif hemisferio.lower() == "sur":
        estacion = determinar_estacion_hemisferio_sur(dia, mes)
        print(f"La estación es: {estacion}")
else:
        print("Hemisferio no reconocido.")

