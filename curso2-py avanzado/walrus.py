# Expresion de asignacion
# WALRUS

# ( nombre := evaluacion)

# Te evitas el uso de variables temporales

def calcularCuadrado(num):
    return num**2

listaNum = range(1,11)

listaPares = []

for num in listaNum:
    # cuadrado = calcularCuadrado(num)
    if (cuadrado := calcularCuadrado(num)) % 2 ==0:
        listaPares.append(cuadrado)
        print(f"El cuadrado de {num} es {cuadrado}, es un numero par")
    else:
        print(f"El cuadrado de {num} es {cuadrado}, es un numero impar")

print(listaPares)

paresComprehension = [cuadrado for num in listaNum if (cuadrado := calcularCuadrado(num))%2 == 0]

print(paresComprehension)