# FUNCION LAMBDA

# lambda x: y            (Funcion anonima> no es definida mediante un nombre en particular)

# lambda: sentencia que invoca la funcion
# x: variable dependiente
# y: cuerpo de la funcion

# Se usa en programacion funcional

# Creas la funcion lambda y la invocas mediante   _( ACA ADENTRO VA EL VALOR A EVALUAR )


# EJEMPLO

# (lambda num: num*2)(2,)

#...................2...........

# multiplicacion = lambda num: num*2
# multiplicacion(3)


# Convertir funciones a lambda

def separarParImpar(listaNumeros):   # Debido a ser una funcion mas compleja, no puede ser convertida en funcion lambda
    pares = []
    impares = []
    for numero in listaNumeros:
        if numero %2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

# ///////////////////////////////////////////
# Son equivalentes

def calcularAreaCuadrado(lado):
    return lado**2

calcularCuadrado = lambda lado: lado **2

print(calcularCuadrado(15))

# ////////////////////////////////////////////

listaNumeros = [1,2,3,4,5,6,7,8,9]

#La primera expresion de lambda verifica si son numeros pares o impares devolviendo true or false. El segundo parametro es la lista de numeros a evaluar. Entonces los que son positivos se quedan, pero "filter" crea un objeto. Por lo tanto hay que convertir ese objeto a una lista mediante la funcion "list".

listaPares = list(filter( lambda numero: numero%2 == 0, listaNumeros))
print(listaPares)

#map nos permite iterar sobre cada uno de los numeros de la "listaNumeros" y los guarda como objeto. Por lo que nuevamente habra que convertirlo en una lista mediante "list".

nuevoLista = list(map(lambda numero: numero*10, listaNumeros))
print(nuevoLista)