# ITERADORES

# iter()    -> permite recorrer el iterable
# next()    -> retorna el elemento siguiente en el iterable

"""
Ciclo for en otros lenguajes
for (inicializador; condicion; iterador) {
    instruccion
}

Ciclo flor en Python
for elementos in list:
    instruccion

"""

nombres = ["Paco", "Emilio", "Javier", "Ana"]

for elemento in nombres:
    if elemento == "Emilio": 
        continue # Sigue el siguiente elemento
        break # Paramos totalmente el ciclo
    print(elemento)

# FOR - ELSE

for nombre in nombres:
    print(nombre)
    if nombre == "Javier":
        break
else:
    print("Ciclo terminado")