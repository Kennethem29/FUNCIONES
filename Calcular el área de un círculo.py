# Función para calcular el área de un círculo
import math

def area_circulo(radio):
    return math.pi * radio**2

# Ejemplo de uso
radio = float(input("Ingresa el radio del círculo: "))
print(f"El área del círculo es: {area_circulo(radio):.2f}")
