""" CSV: Commas separated values """

""" Representan tablas """

import csv
import os

rutaNombre = "csv_vacio.csv"
rutaRelativa = "./curso2-py avanzado/csv/csv_vacio.csv"
rutaRelativa2 = "./curso2-py avanzado/csv/datos2.csv"
rutaAbsolutaOS = os.path.join(os.getcwd(), rutaNombre)

archivoAbierto = open(rutaRelativa, "w")
writer = csv.writer(archivoAbierto, delimiter=",")

archivoAbierto.close()

print(rutaAbsolutaOS)

columnas = ["nombre", "apellido", "edad"]
dato = ["Paco", "Botero", 26]

datos_lista = [
    ["Paco", "Botero", 26],
    ["Javier", "Quiñonez", 24],
    ["Emilio", "Tafur", 25]
]
datos_dict = [
    {"nombre": "Paco", "apellido": "Botero", "edad": 26},
    {"nombre": "Javier", "apellido": "Quiñonez", "edad": 24},
    {"nombre": "Emilio", "apellido": "Tafur", "edad": 25}
]

with open('./curso2-py avanzado/csv/datos.csv', "w", newline="") as archivo:
    writer = csv.writer(archivo, delimiter = ",")
    writer.writerow(columnas)
    writer.writerows(datos_lista)

with open(rutaRelativa2, "w", newline="") as archivo:
    writer = csv.DictWriter(archivo, fieldnames= columnas)
    writer.writeheader()
    writer.writerows(datos_dict)