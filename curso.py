print("hello world")

# Comentario

int(3.23) # Devuelve el entero
float(5) # Convierte a punto flotante
str(True) # convierte a string
type("texto") # Devuelve el tipo de variable
help() # Podes pedir documentacion de funciones

# Estructura de datos #

listas = [1, 2, 'palabra1', 'palabra2']
len(listas) # Devuelve longitud de lista
listas[2] # Acceso; Pueden usarse numeros negativos
listas[0:2] # Devuelve el rango pedido

listaAnidada = ['java', 'javascript', listas]

listas.append('palabra3') # A;adir al final

otrosLenguajes = ['c', 'c++']

listas.extend(otrosLenguajes) # Extiende la lista, no a;ade toda la lista al ultimo lugar.


tuplas = ('python', 'c', 'c++') # No pueden alterarse, requieren menor tiempo de procesamiento

diccionarios = { "nombre": "python", "creador": "cualquiera"} # Son analogos a los Json.
diccionarios.keys()  # Devuelve las variables
diccionarios.items() # Devuelve todos los items ordenados
diccionarios.values() # Devuelve los valores

set = { 1, 2, 3} # No guardan informacion repetida. No se puede acceder a un indice. Son mutables pero no las variables.
set.add(4)
set.update([4,5,6])
len(set)
set.discard(2) # No elimina el indice, elimina el numero buscado
set.remove(3)
set.clear() # Lo deja vacio

# Expresiones condicionales #

# is, and, or, not

if 1>2:
    print('if block')
elif 1<2:
    print('elif block')
else:
    print('else')

# CICLO FOR

#for <element> in <object>:
    #instrucciones

for letra in "Texto":
    print(letra)

for numero in range(1,5):
    print(numero)

listaPrueba1 = ['prueba1', 'prueba2', 'prueba3']

for index in range(len(listaPrueba1)):  # Iterar listas
    print('Index: ', index)
    print('Elemento: ', listaPrueba1[index])

for llave, valor in diccionarios.items():
    print(llave, valor) # Aca pueden tomarse dos variables porque items devuelve una serie de duplas.

# CICLO WHILE

#while <condicion>:
    #instrucciones

i=1
while i <=5:
    print(i)
    if i == 3:
        break
    i+= 1

j = 0
while j < len(listaPrueba1):
    print(listaPrueba1)
    j += 1