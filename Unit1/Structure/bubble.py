lista = [40,21,4,9,10,35]

def ordenamiento(lista):
    intercambios = True
    numPasada = len(lista)-1
    n = 0
    while numPasada > 0 and intercambios:
        intercambios = False
        n += 1
        for i in range(numPasada):
            if lista[i]>lista[i+1]:
                intercambios = True
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
        numPasada = numPasada-1
        print('Pasada',n,lista)
    

ordenamiento(lista)
