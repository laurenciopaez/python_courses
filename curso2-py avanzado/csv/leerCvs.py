import csv

with open("curso2-py avanzado\csv\datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    columnas = next(reader)
    print("Columnas", columnas)
    for fila in reader:
        print(f"{fila[0]} edad {fila[2]}")


with open("curso2-py avanzado\csv\datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila)
        print(fila["nombre"])

