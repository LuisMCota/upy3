lista = [11,7,8,2,0,6,10,1]

def ordSeleccion(lista):
    longitud = len(lista)
    for i in range(longitud-1):
        indicemenor = i
        for j in range(i+1, longitud):
            if lista[indicemenor] > lista[j]:
                lista[indicemenor], lista[j] = lista[j], lista[indicemenor]


ordSeleccion(lista)
print(lista)