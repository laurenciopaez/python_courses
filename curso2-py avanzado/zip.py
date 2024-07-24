# Funcion ZIP()

# Devuelve un objeto iterador
# Es utilizado comunmente en bucles for para procesar elementos de manera paralela desde varias estructuras de datos

nombres=["Paco", "Emilio", "Javier", "Ana"]
apellidos=["Botero", "Tafur", "Quinionez"]

nombresCompletos = list(zip(nombres, apellidos)) # Se estan creando las tuplas. Todos tienen que tener su par correspondiente, sino no se toma en cuneta.
print(nombresCompletos)

nombres_unzip, apellidos_unzip = zip(*nombresCompletos)

print(nombres_unzip)
print(apellidos_unzip)

for nombre, apellido in zip(nombres, apellidos):
    print(nombre, apellido)

