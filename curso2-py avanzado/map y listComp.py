def calcularCuadrado(numero):
    return numero**2

listaNum = range(1,11)
listaCuadrados = []
""" 
for num in listaNum:
    cuadrado = calcularCuadrado(num)
    listaCuadrados.append(cuadrado)

print(listaCuadrados) 

"""

mapCuadrados = list(map(calcularCuadrado, listaNum))
print(mapCuadrados)

""" 
LIST COMPREHENSION

lista = [ expresion(elemento) for elemento in objeto_iterable ]

"""

lista = [ calcularCuadrado(elemento) for elemento in listaNum]

lista2 = [ elemento**3 for elemento in listaNum]

print(lista)
print(lista2)

listaIf = [ elemento*10 for elemento in listaNum if elemento%2 == 0] # La condicion puede ser una funcion tambien.

print(listaIf)

listaIf2 = [elemento*10 if elemento%2 == 0 else 0 for elemento in listaNum]

print(listaIf2)

# No se repiten los numeros al definir el Set

listaNum2 = [1,2,2,2,3,4,5,6,7,8,9]

setPares = {num for num in listaNum2 if num%2 ==0}
print(setPares)

vocales = "aeiou"
diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}
print(diccionario)