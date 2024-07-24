"""
enumerate(iterable, start=0)

"""

nombres= ["Paco", "Emilio", "Javier", "Ana"]

nombresEnumerados = enumerate(nombres, 3)
print(list(nombresEnumerados))
# Resultado: [(3, 'Paco'), (4, 'Emilio'), (5, 'Javier'), (6, 'Ana')]

for indice, elemento in enumerate(nombres):   # El indice inicia en 0
    print(indice, elemento)