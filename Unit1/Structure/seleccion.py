lista = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]

def ordSeleccion(lista):
    longitud = len(lista)
    for i in range(longitud-1):
        indicemenor = i
        for j in range(i+1, longitud):
            if lista[indicemenor] > lista[j]:
                lista[indicemenor], lista[j] = lista[j], lista[indicemenor]


ordSeleccion(lista)
print(lista)