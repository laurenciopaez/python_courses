def funcion1():
    # Instrucciones
    print('Imprime funcion')


funcion1()

def perimetroCuadrado(lado, unidades):
    perimetro = lado *4
    print(f"El perimetro es {perimetro} {unidades}")

perimetroCuadrado(4, "mm")
perimetroCuadrado(lado= 5, unidades= "metros")

def areaCuadradoyPerimetro(lado):
    """Calcula el area y perimetro de un cuadrado""" # Descripcion de una funcion. Al llamarla te dice lo que hace 
    area = lado*lado
    perimetro = lado *4
    return area, perimetro

area = areaCuadradoyPerimetro(lado=5)
print(area)