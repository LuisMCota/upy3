def ordenacion_seleccion(lista):
    for numero in range(len(lista)-1,0,-1):
        indiceMax = 0
        for i in range(1,numero+1):
            if lista[i] > lista[indiceMax]:
                indiceMax = i
        
        temporal = lista[numero]
        lista[numero] = lista[indiceMax]
        lista[indiceMax] = temporal

lista = [1,4,5,6,3,7,8,2,10,9]
ordenacion_seleccion(lista)
print(lista)

def ordenacion_insercion(lista):
    for indice in range(1, len(lista)):    #indice va de 1, casilla por casilla 
        valor = lista[indice]    #toma la posición del bloque, es decir el indice 
        posicion = indice 

        while posicion > 0 and lista [posicion -1]> valor: # define el valor e indica si quiere agregar algo nuevo 
            lista[posicion] = lista[posicion - 1]           # toma otra posicion y le da otro valor 
            posicion -= 1                                  
            lista[posicion] = valor                   
            
ordenacion_insercion(lista)
print(lista)