from modulos.auxiliar import areaCuadrado, perimetroCuadrado
from modulos.circulo import areaCirculo, perimetroCirculo

lado = 5
radio = 5
cuadrado = {
    "lado": lado,
    "perimetro": perimetroCuadrado(lado),
    "area": areaCuadrado(lado)
}
circulo = {
    "radio": radio,
    "perimtro": perimetroCirculo(radio),
    "area": areaCirculo(radio=radio)
}

print(cuadrado, circulo)