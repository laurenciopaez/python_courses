# paramaetro> nombre del argumento
# argumento> variable asignada
# *args> parametros opcionales en forma de lista
# **kwargs> parametros opcionales en forma de diccionario (argumentos de palabra clave)
# retorno> lo que devuelve

def calcularPerimetro(*args): #args pasa como una tupla
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro

perimetro = calcularPerimetro(1,5,7,9,2,4) #podes pasarle todos los parametros que quieras
print(perimetro)

def funcionKwargs(**kwargs):
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")

funcionKwargs(nombre="Paco", apellido="Botero")

# ORDEN DE PARAMETROS

def parametros(parametros, *args, **kwargs):
    pass