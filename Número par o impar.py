# Función para verificar si un número es par
def es_par(numero):
    return numero % 2 == 0

# Ejemplo de uso
numero = int(input("Ingresa un número: "))
resultado = es_par(numero)
print(f"El número {numero} es {'par' if resultado else 'impar'}.")
