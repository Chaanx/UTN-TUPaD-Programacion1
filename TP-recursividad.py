# Ejercicio 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

mostrar_factoriales(5)


# # Ejercicio 2


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci(hasta):
    serie = [fibonacci(i) for i in range(hasta + 1)]
    print("Serie de Fibonacci:", serie)

mostrar_fibonacci(10)


# Ejercicio 3


def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

print(potencia(2, 5))


# # Ejercicio 4


def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario(n):
    resultado = decimal_a_binario(n)
    return resultado if resultado else "0"

print(convertir_a_binario(10))

# # Ejercicio 5


def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print(es_palindromo("reconocer"))


# # Ejercicio 6



def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(1234))


#  Ejercicio 7


def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

print(contar_bloques(4))

# Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

print(contar_digito(12233421, 2))