def calcularPromedio(lista):
    assert len(lista) > 0, "La lista esta vacia"
    return sum(lista)/len(lista)

try:
    promedio = calcularPromedio(lista=['Texto'])
    print(promedio)
except AssertionError as assert_error:
    print(assert_error)
except Exception as error:
    print('La funcion no calculo el promedio')
    print(error)

    